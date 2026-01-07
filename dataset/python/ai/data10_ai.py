from typing import List


def quicksort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the QuickSort algorithm (Pythonic version).
    Does not mutate the input list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    data = [3, 7, 2, 5, 8, 4, 9, 1, 6]
    print(quicksort(data))
