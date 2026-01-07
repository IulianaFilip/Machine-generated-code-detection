import random

def ai_merge_sort_algorithm(input_array):
    if len(input_array) <= 1:
        return input_array
    
    middle_index = len(input_array) // 2
    left_subarray = ai_merge_sort_algorithm(input_array[0:middle_index])
    right_subarray = ai_merge_sort_algorithm(input_array[middle_index:])
    
    merged_array = ai_merge_two_arrays(left_subarray, right_subarray)
    return merged_array

def ai_merge_two_arrays(left_array, right_array):
    merged_result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged_result.append(left_array[left_index])
            left_index += 1
        else:
            merged_result.append(right_array[right_index])
            right_index += 1
    
    # Append remaining elements
    merged_result.extend(left_array[left_index:])
    merged_result.extend(right_array[right_index:])
    
    return merged_result

if __name__ == "__main__":
    rd = random.Random()
    rd.seed(0)
    
    temp_list = list(range(0, 10))
    rd.shuffle(temp_list)
    
    print("Initial array:", temp_list)
    sorted_array = ai_merge_sort_algorithm(temp_list)
    print("Sorted array:", sorted_array)
