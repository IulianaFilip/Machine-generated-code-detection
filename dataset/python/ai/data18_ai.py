def ai_complex_number_multiplication(real_part_a, imag_part_a, real_part_b, imag_part_b):
    # Step 1: multiply real parts
    product_real_real = real_part_a * real_part_b
    
    # Step 2: multiply imaginary parts
    product_imag_imag = imag_part_a * imag_part_b
    
    # Step 3: multiply sum of parts
    sum_of_a_parts = real_part_a + imag_part_a
    sum_of_b_parts = real_part_b + imag_part_b
    product_sum_parts = sum_of_a_parts * sum_of_b_parts
    
    # Step 4: calculate real component of result
    result_real = product_real_real - product_imag_imag
    
    # Step 5: calculate imaginary component of result
    result_imag = product_sum_parts - product_real_real - product_imag_imag
    
    # Step 6: return the final complex multiplication result
    return result_real, result_imag

# Example usage
if __name__ == "__main__":
    a_real, a_imag = 3, 2
    b_real, b_imag = 1, 4
    real_result, imag_result = ai_complex_number_multiplication(a_real, a_imag, b_real, b_imag)
    print("Result of multiplication: Real =", real_result, ", Imag =", imag_result)
