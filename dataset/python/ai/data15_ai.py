import random

rd = random.Random()
rd.seed(0)

def quick_select_algorithm(arr, k):
    left_part, middle_part, right_part = partition_three(arr)
    if k <= len(left_part):
        return quick_select_algorithm(left_part, k)
    elif k > len(left_part) + len(middle_part):
        return quick_select_algorithm(right_part, k - len(left_part) - len(middle_part))
    else:
        return middle_part[0]

def partition_three(arr):
    left_list = []
    middle_list = []
    right_list = []
    pivot_index = random.choice(range(len(arr)))
    pivot_value = arr[pivot_index]
    for element in arr:
        if element < pivot_value:
            left_list.append(element)
        elif element == pivot_value:
            middle_list.append(element)
        else:
            right_list.append(element)
    return left_list, middle_list, right_list

def quick_select_in_place(arr, k):
    return quick_select_in_place_helper(arr, 0, len(arr)-1, k)

def quick_select_in_place_helper(arr, low_index, high_index, k):
    left, middle, right = partition_three_in_place(arr, low_index, high_index)
    left_length = middle - left
    middle_length = right - middle
    right_length = high_index - right + 1

    if k <= left_length:
        return quick_select_in_place_helper(arr, left, middle-1, k)
    elif k > left_length + middle_length:
        return quick_select_in_place_helper(arr, right, high_index, k - left_length - middle_length)
    else:
        return arr[middle]

def partition_three_in_place(arr, lb, ub):
    pivot_index = random.choice(range(lb, ub+1))
    pivot_value = arr[pivot_index]

    low = lb
    high = ub

    while low < high:
        while low < high and arr[low] <= pivot_value:
            low += 1
        while low < high and arr[high] > pivot_value:
            high -= 1
        arr[low], arr[high] = arr[high], arr[low]

    if arr[low] > pivot_value:
        arr[low-1], arr[pivot_index] = arr[pivot_index], arr[low-1]
    else:
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    left = lb
    middle = arr.index(pivot_value)
    right = ub + 1

    for i in range(middle, ub+1):
        if arr[i] != pivot_value:
            right = i
            break

    return left, middle, right

if __name__ == "__main__":
    my_list = list(range(10))
    rd.shuffle(my_list)

    for i in range(1, 11):
        value = quick_select_in_place(my_list, i)
        print("The", i, "th smallest value is:", value)
