# Simple fraction to mixed number converter
# Level: 5kyu
'''
Problem Description: Division by zero should raise an error (preferably, the standard zero division error
of your language).
Examples

    Input: 42/9, expected result: 4 2/3.
    Input: 6/3, expedted result: 2.
    Input: 4/6, expected result: 2/3.
    Input: 0/18891, expected result: 0.
    Input: -10/7, expected result: -1 3/7.
    Inputs 0/0 or 3/0 must raise a zero division error.

Note

Make sure not to modify the input of your function in-place, it is a bad practice.
'''


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def mixed_fraction(s):
    arr = s.split('/')
    num, den = [int(i) for i in arr]
    if den == 0:
        raise ZeroDivisionError
    else:
        if num % den == 0:
            return str(num//den)
        elif abs(num) < abs(den):
            return str(num//gcd(num, den)) + '/' + str(den//gcd(num, den))
        else:
            if (num < 0 and den > 0) or (num > 0 and den < 0):
                return '-' + str(abs(num)//abs(den)) + ' ' + str((abs(num) % abs(den))//gcd(abs(num), abs(den))) + '/' + str(abs(den)//gcd(abs(num), abs(den)))
            else:
                return str(num//den) + ' ' + str((num % den)//gcd(num, den)) + '/' + str(den//gcd(num, den))

# Test Cases

print(mixed_fraction('-22/-7'))
print(mixed_fraction('-10/7'))
print(mixed_fraction('42/9'))
print(mixed_fraction('6/3'))
print(mixed_fraction('4/6'))
print(mixed_fraction('0/18891'))
print(mixed_fraction('0/0'))
