# Identical Elements
# Level: 7kyu
'''
Problem Description: Given two arrays of integers m and n, test if they contain at least one identical 
element. Return true if they do; false if not.

Your code must handle any value within the range of a 32-bit integer, and must be capable of handling 
either array being empty (which is a false result, as there are no duplicated elements).
'''

def duplicate_elements(m, n):
	if len(m) == 0 or len(n) == 0:
		return False
	m = set(m)
	n = set(n)
	c = 0
	for i in m:
		if i in n:
			c += 1

	if c == 0 or c == len(m):
		return False
	else:
		return True

# Test Case

print(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9])) 
print(duplicate_elements([9, 8, 7], [8, 1, 3]))
print(duplicate_elements([1], [1]))
print(duplicate_elements([1], []))