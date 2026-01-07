from typing import List


def quicksort(values: List[int]) -> List[int]:
    """
    Sort a list of integers using the QuickSort algorithm.
    """
    if len(values) <= 1:
        return values

    pivot = values[-1]
    left = [x for x in values[:-1] if x < pivot]
    right = [x for x in values[:-1] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    data = [3, 7, 2, 5, 8, 4, 9, 1, 6]
    print(quicksort(data))
