"""
MOF_Dimensions_CIF.py

Processes CIF structures by performing two expansions of a polymeric network
and computes minimum-area bounding boxes. The comparison of bounding boxes
is used to determine the dimensionality of the framework.

Original script:
- S.B. Wiggin, Cambridge Crystallographic Data Centre (2020)
- Modified by Olivier Marchand, University of Ottawa (2024)

Refactored for clarity, modularity, and Pythonic style.
"""

from __future__ import annotations

import argparse
import csv
import os
import time
from typing import Iterable, Tuple

import numpy as np
from ccdc.io import EntryReader


# -----------------------------
# Geometry utilities
# -----------------------------

def compute_bounding_box_lengths(atoms: Iterable) -> np.ndarray:
    """
    Compute the sorted lengths of the principal axes of a bounding box
    enclosing the given atoms.

    Parameters
    ----------
    atoms : Iterable
        Atoms with 3D coordinates.

    Returns
    -------
    np.ndarray
        Sorted array of bounding box axis lengths.
    """
    points = np.array([atom.coordinates for atom in atoms])
    covariance_matrix = np.cov(points, rowvar=False)

    eigenvalues, _ = np.linalg.eig(covariance_matrix)
    lengths = np.sqrt(eigenvalues)

    # Prevent zero-length dimensions
    return np.sort(lengths + 1e-4)


# -----------------------------
# Dimensionality analysis
# -----------------------------

def compute_framework_dimensionality(entry) -> int:
    """
    Determine the dimensionality of a polymeric framework by comparing
    bounding boxes from two different expansion sizes.

    Parameters
    ----------
    entry
        CCDC crystal entry.

    Returns
    -------
    int
        Number of growing dimensions (0–3).
    """
    start_time = time.time()

    expansion_small = entry.crystal.polymer_expansion(repetitions=4)
    expansion_large = entry.crystal.polymer_expansion(repetitions=7)

    elapsed_time = time.time() - start_time
    print(f"Polymer expansion time: {elapsed_time:.2f}s")

    lengths_small = compute_bounding_box_lengths(expansion_small.atoms)
    lengths_large = compute_bounding_box_lengths(expansion_large.atoms)

    print(f"Atoms (small expansion): {len(expansion_small.atoms)}")
    print(f"Atoms (large expansion): {len(expansion_large.atoms)}")

    growth_ratios = lengths_large / lengths_small
    print(f"Growth ratios: {growth_ratios.tolist()}")

    threshold = 1.15
    return int(np.sum(growth_ratios > threshold))


def classify_dimensionality(ndims: int) -> str:
    """
    Convert a numeric dimensionality into a human-readable label.
    """
    labels = {
        0: "0D non-MOF",
        1: "1D chain",
        2: "2D sheet",
        3: "3D framework",
    }
    return labels.get(ndims, "Unknown")


# -----------------------------
# CIF processing
# -----------------------------

def process_cif_file(
    cif_path: str,
    writer: csv.writer,
    structure_index: int,
) -> Tuple[int, int, int]:
    """
    Analyze all structures in a CIF file and append results to CSV.

    Returns
    -------
    Tuple[int, int, int]
        Updated structure index, number of MOFs, number of non-MOFs.
    """
    mof_count = 0
    non_mof_count = 0

    try:
        reader = EntryReader(cif_path, format="cif")

        for entry in reader:
            structure_index += 1
            print(f"\nProcessing CIF entry: {entry.identifier}")

            polymer_components = [
                component
                for component in entry.molecule.components
                if component.is_polymeric
            ]

            if len(polymer_components) > 1:
                print("Warning: multiple polymeric components detected")

            if entry.molecule.heaviest_component.is_polymeric:
                mof_count += 1
                framework = entry.molecule.heaviest_component
                framework.remove_hydrogens()
                entry.crystal.molecule = framework

                ndims = compute_framework_dimensionality(entry)
                dimension_label = classify_dimensionality(ndims)
            else:
                non_mof_count += 1
                dimension_label = "No polymeric bonds detected"

            print(
                f"Framework dimensionality for {entry.identifier}: {dimension_label}"
            )
            writer.writerow((entry.identifier, dimension_label, structure_index))

    except Exception as exc:
        filename = os.path.basename(cif_path)
        print(f"\nFailed to process CIF file {filename}:\n{exc}")
        writer.writerow((filename, "FAILED", structure_index))
        structure_index += 1

    return structure_index, mof_count, non_mof_count


# -----------------------------
# CLI handling
# -----------------------------

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="MOF dimensionality analysis from CIF files")
    parser.add_argument("-i", "--input", required=True, help="Directory containing CIF files")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file")

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    structure_index = 0

    with open(args.output, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(("Filename", "Dimensionality", "File Order"))

        for filename in os.listdir(args.input):
            cif_path = os.path.join(args.input, filename)
            if os.path.isfile(cif_path):
                structure_index, _, _ = process_cif_file(
                    cif_path, writer, structure_index
                )


if __name__ == "__main__":
    main()
