# Descending Order
# Level: 7kyu
'''
Problem Description: Your task is to make a function that can take any non-negative integer as a 
argument and return it with it's digits in descending order. Descending order means that you take the 
highest digit and place the next highest digit immediately after it.
Examples:

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
'''


def Descending_Order(num):
    # Bust a move right here
    return int(''.join([str(i) for i in sorted([int(i) for i in list(str(num))], reverse=True)]))

# Test Case

print(Descending_Order(53242323))
