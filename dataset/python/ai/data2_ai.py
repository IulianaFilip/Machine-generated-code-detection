"""
MOF_Dimensions_CIF_Parallel.py

Processes CIF structures by performing two expansions of a polymeric network
and computes minimum-area bounding boxes. The comparison of bounding boxes
is used to determine the dimensionality of the framework.

This version supports parallel execution for improved performance.

Original script:
- S.B. Wiggin, Cambridge Crystallographic Data Centre (2020)
- Modified by Olivier Marchand, University of Ottawa (2024)
"""

from __future__ import annotations

import argparse
import csv
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Iterable, List, Tuple

import numpy as np
from ccdc.io import EntryReader


# -----------------------------
# Result collection
# -----------------------------

class ResultCollector:
    """
    Collects and prints diagnostic information during processing.
    """

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        self.messages: List[str] = []

    def add(self, message: str) -> None:
        self.messages.append(message)

    def flush(self) -> None:
        print(f"\nCIF file: {self.identifier}")
        for message in self.messages:
            print(message)


# -----------------------------
# Geometry utilities
# -----------------------------

def compute_bounding_box_lengths(atoms: Iterable) -> np.ndarray:
    """
    Compute sorted bounding box axis lengths from atomic coordinates.
    """
    points = np.array([atom.coordinates for atom in atoms])
    covariance = np.cov(points, rowvar=False)

    eigenvalues, _ = np.linalg.eig(covariance)
    lengths = np.sqrt(eigenvalues)

    return np.sort(lengths + 1e-4)


# -----------------------------
# Dimensionality analysis
# -----------------------------

def compute_dimensionality(entry, collector: ResultCollector) -> int:
    """
    Determine framework dimensionality by comparing two polymer expansions.
    """
    start = time.time()

    small_expansion = entry.crystal.polymer_expansion(repetitions=4)
    large_expansion = entry.crystal.polymer_expansion(repetitions=7)

    elapsed = time.time() - start
    collector.add(f"Polymer expansion time: {elapsed:.2f} seconds")

    lengths_small = compute_bounding_box_lengths(small_expansion.atoms)
    lengths_large = compute_bounding_box_lengths(large_expansion.atoms)

    collector.add(f"Atoms (small expansion): {len(small_expansion.atoms)}")
    collector.add(f"Atoms (large expansion): {len(large_expansion.atoms)}")

    growth_ratios = lengths_large / lengths_small
    collector.add(f"Growth ratios: {growth_ratios.tolist()}")

    threshold = 1.15
    return int(np.sum(growth_ratios > threshold))


def dimensionality_label(ndims: int) -> str:
    """
    Convert numeric dimensionality into a human-readable label.
    """
    return {
        0: "0D non-MOF",
        1: "1D chain",
        2: "2D sheet",
        3: "3D framework",
    }.get(ndims, "Unknown")


# -----------------------------
# CIF processing
# -----------------------------

def process_cif(cif_path: str) -> List[Tuple[str, str]]:
    """
    Analyze a CIF file and return dimensionality results.

    Returns
    -------
    List[Tuple[str, str]]
        (entry identifier, dimensionality label)
    """
    results: List[Tuple[str, str]] = []

    try:
        reader = EntryReader(cif_path, format="cif")

        for entry in reader:
            collector = ResultCollector(entry.identifier)
            dimension = "No polymeric bonds detected"

            if any(component.is_polymeric for component in entry.molecule.components):
                framework = entry.molecule.heaviest_component
                framework.remove_hydrogens()
                entry.crystal.molecule = framework

                ndims = compute_dimensionality(entry, collector)
                dimension = dimensionality_label(ndims)

                collector.add(f"Framework dimensionality: {dimension}")

            collector.flush()
            results.append((entry.identifier, dimension))

            del collector
            del entry

    except Exception as exc:
        filename = os.path.basename(cif_path)
        print(f"\nFailed to process CIF file {filename}:\n{exc}")
        results.append((filename, "FAILED"))

    return results


# -----------------------------
# CLI handling
# -----------------------------

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parallel MOF dimensionality analysis from CIF files"
    )
    parser.add_argument("-i", "--input", required=True, help="Input CIF directory")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file")
    parser.add_argument(
        "-n",
        "--num-cpus",
        type=int,
        default=1,
        help="Number of CPUs to use (default: 1)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    cif_files = [
        os.path.join(args.input, filename)
        for filename in os.listdir(args.input)
        if os.path.isfile(os.path.join(args.input, filename))
    ]

    with open(args.output, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(("Filename", "Dimensionality"))

        with ProcessPoolExecutor(max_workers=args.num_cpus) as executor:
            futures = {
                executor.submit(process_cif, cif_path): cif_path
                for cif_path in cif_files
            }

            for future in as_completed(futures):
                for record in future.result():
                    writer.writerow(record)
                csv_file.flush()


if __name__ == "__main__":
    main()
