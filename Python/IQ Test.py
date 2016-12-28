# IQ Test
# Level: 6kyu
'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the 
given numbers differs from the others. Bob observed that one number usually differs from the others in 
evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one 
that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements 
start from 1 (not 0)
Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest odd
'''


def iq_test(numbers):
    div_arr = [int(i) % 2 for i in numbers.split()]
    m = 0
    if div_arr.count(1) > div_arr.count(0):
        m = 0
    else:
        m = 1
    return div_arr.index(m) + 1

# Test Cases

print(iq_test("2 4 7 8 10"))
print(iq_test("1 4 3 45 13"))
