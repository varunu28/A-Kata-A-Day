# Coprime Validator
# Level: Beta
'''
Write a program to determine if two numbers are coprime. A pair of numbers are coprime if their 
greatest shared factor is 1. For example:

20 and 27
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 27: 1, 3, 9, 27
Greatest shared factor: 1
20 and 27 are coprime

An example of two numbers that are not coprime:

12 and 39
Factors of 12: 1, 2, 3, 4, 6, 12
Factors of 39: 1, 3, 13, 39
Greatest shared factor: 3
12 and 39 are not coprime

If the two inputs are coprime, your program should return true. If they are not coprime, your program 
should return false.
'''

def are_coprime(n,m):
	fact = []
	i = 1
	while i <= min(n,m)//2:
		if min(n,m)%i == 0:
			fact.append(i)
		i += 1
	fact.append(min(n,m))

	i = 1
	while i <= max(n,m)//2:
		if max(n,m)%i == 0:
			if i != 1 and i in fact:
				return False
		i += 1
	return True

# Test Cases

print(are_coprime(20,27))
print(are_coprime(12,39))
print(are_coprime(17,34))