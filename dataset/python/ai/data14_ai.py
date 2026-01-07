def count_inversion(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0
    mid = n // 2
    left_part, left_count = count_inversion(arr[:mid])
    right_part, right_count = count_inversion(arr[mid:])
    merged_arr, split_count = merge_and_count(left_part, right_part)
    total_count = left_count + right_count + split_count
    return merged_arr, total_count

def merge_and_count(left, right):
    merged = []
    i = 0
    j = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged, count

def find_first_greater(array, target):
    low = 0
    high = len(array)
    while low < high:
        m
