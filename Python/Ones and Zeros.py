# Ones and Zeros
# Level: 7kyu
'''
Problem Description: Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
'''


def binary_array_to_number(arr):
    i = 0
    n = len(arr)-1
    num = 0
    while n >= 0:
        num += arr[n]*pow(2, i)
        i += 1
        n -= 1
    return num

# Test Case

print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 1, 1, 0]))
