from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the Insertion Sort algorithm.
    Returns a new sorted list without mutating the input.
    """
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print(insertion_sort(data))
