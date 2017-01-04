# Square Every Digit
# Level: 7kyu
'''
Problem Description: Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
'''


def square_digits(num):
    ans = ''
    for i in str(num):
        ans += str(int(i)**2)
    return int(ans)

print(square_digits(9119))
