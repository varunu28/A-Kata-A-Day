# Even Fibonacci Sum
# Level: 6kyu
'''
Problem Statement:Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the 
maximum value.

The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The 
series starts with 0 and 1:

0 1 1 2 3 5 8 13 21...

For example:

eve_fib(0)==0
eve_fib(33)==10
eve_fib(25997544)==19544084
'''

def even_fib(m):
	if m == 0 or m == 1:
		return 0
	else:
		arr = []
		a = 0
		b = 1
		c = 0
		while c < m:
			c = a+b
			if c%2 == 0 and c < m:
				arr.append(c)
			a = b
			b = c
		return sum(arr)

# Test Cases

print(even_fib(33))
print(even_fib(25997544))
print(even_fib(1))
print(even_fib(10))
print(even_fib(5))
