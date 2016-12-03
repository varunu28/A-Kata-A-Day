# Number of trailing zeros of N!
# Level: 5kyu
'''
Problem Description: Write a program that will calculate the number of trailing zeros in a factorial 
of a given number.

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
'''

def zeros(n):
	count = 0
	while n > 0:
		count += n//5
		n = n//5
	return count

# Test Cases

print(zeros(5))
print(zeros(10))
print(zeros(12))