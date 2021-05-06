# Gap in Primes
# Level: 5 Kyu
'''
Problem Description: The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. 
From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps 
primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer >= 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 2, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 2 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language). In C++ return in such a case {0, 0}.
Examples:

gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil or in C++ {0, 0}

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.
'''


def gap(g, m, n):
    last_prime = 2
    for i in range(m, n+1):
        prime = True

        for j in range(2, int(n**.5)+1):
            if i % j == 0:
                prime = False
                break

        if prime:
            if i - last_prime == g:
                return [last_prime, i]
            else:
                last_prime = i

# Test Cases

print(gap(2, 100, 110))
print(gap(4, 100, 110))
print(gap(6, 100, 110))
print(gap(8, 300, 400))
print(gap(10, 300, 400))


# The above codes do not return the desrired outputs. For example when you enter [8, 5, 13] it returns None istead of [5, 13]. 
# To solve this bug, I have firstly used    "if i - sample_prime == g and sample_prime in range(m, n + 1):". However, this has not
# solved other bugs - (10, 600, 700) should retun [607, 617], yours returns [631, 641]. Therefore, I suggest a completely different 
# code. 

def prime(start,stop):
    prime_list = []
    for i in range(start, stop + 1):
        for ii in range(2, int(i ** 0.5) + 1):
            if i % ii == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

def prime_gap(start, stop, gap):
    prime_list = prime(start, stop)
    for x in range(len(prime_list)):
        for y in range(x):
            if prime_list[x] - prime_list[y] == gap:
                return prime_list[y], prime_list[x]
    else:
        return "None"
            
print(prime_gap(600, 700, 10))
