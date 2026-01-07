import numpy as np
import random

rd = random.Random()
rd.seed(0)

def mom_select_algorithm(arr, k):
    if len(arr) < 50:
        return quick_select_algorithm(arr, k)
    
    reshaped_array = list(np.reshape(arr, (5, -1)).transpose())
    median_list = [quick_select_algorithm(list(row), 3) for row in reshaped_array]
    
    pivot_value = mom_select_algorithm(median_list, len(arr) // 10)
    
    left_partition, middle_partition, right_partition = partition_three_with_pivot(arr, pivot_value)
    
    if k <= len(left_partition):
        return mom_select_algorithm(left_partition, k)
    elif k > len(left_partition) + len(middle_partition):
        return mom_select_algorithm(right_partition, k - len(left_partition) - len(middle_partition))
    else:
        return pivot_value

def partition_three_with_pivot(arr, pivot_value):
    left_list = []
    middle_list = []
    right_list = []
    for element in arr:
        if element < pivot_value:
            left_list.append(element)
        elif element == pivot_value:
            middle_list.append(element)
        else:
            right_list.append(element)
    return left_list, middle_list, right_list

def quick_select_algorithm(arr, k):
    left_partition, middle_partition, right_partition = partition_three_random(arr)
    if k <= len(left_partition):
        return quick_select_algorithm(left_partition, k)
    elif k > len(left_partition) + len(middle_partition):
        return quick_select_algorithm(right_partition, k - len(left_partition) - len(middle_partition))
    else:
        return middle_partition[0]

def partition_three_random(arr):
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

if __name__ == "__main__":
    my_list = list(range(60))
    rd.shuffle(my_list)
    
    for i in range(1, 61):
        value = mom_select_algorithm(my_list, i)
        print("The", i, "th smallest value is:", value)
