from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the Selection Sort algorithm.
    Returns a new sorted list without mutating the input.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]

    return sorted_arr


if __name__ == "__main__":
    data = [7, 3, 9, 2, 5, 10, 6, 1, 4, 8]
    print("Sorted list:", selection_sort(data))
