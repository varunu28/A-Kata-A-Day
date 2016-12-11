# Fizz / Buzz
# Level: 6kyu
'''
Problem Description: Write a function that takes an integer and returns an Array [A, B, C] where A is 
the number of multiples of 3 (but not 5) less than the given integer, B is the number of multiples of 
5 (but not 3) less than the given integer and C is the number of multiples of 3 and 5 less than the 
given integer.

For example, solution(20) should return [5, 2, 1]
'''

def solution(number):
	only_3 = 0
	only_5 = 0
	both = 0
	i = 1
	while i < number:
		if i%3 == 0 and i%5 == 0:
			both += 1
		elif i%3 == 0:
			only_3 += 1
		elif i%5 == 0:
			only_5 += 1
		i += 1

	ans = [only_3, only_5, both]
	return ans

# Test Cases

print(solution(20))
print(solution(2))
print(solution(30))
print(solution(300))


