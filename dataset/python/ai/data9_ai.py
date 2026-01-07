from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort a list of integers using the Merge Sort algorithm.
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [24, 3, -10, 7, 5, -5, 12, 0]
    print(merge_sort(data))
