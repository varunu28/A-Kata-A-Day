# Is a number prime?
# Level: 6kyu
'''
Problem Description: Define a function isPrime that takes one integer argument and returns true or 
false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive 
divisors other than 1 and itself.

Example

isPrime(5)
=> true

Assumptions

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers.
'''


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    j = 4
    while j <= num/2:
        if num % j == 0:
            return False
        j += 1
    return True
