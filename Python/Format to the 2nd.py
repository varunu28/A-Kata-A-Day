# Format to the 2nd
# Level: 7kyu
'''
Problem Description: Given some positive integers, I wish to print the integers such that all take up 
the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the 
largest integer.

For example, given 1, 23, 2, 17, 102, the following string should be printed out:

001
023
002
017
102

Write a function print_nums(n1, n2, n3, ...) that takes a variable number of arguments and returns the 
string to be printed out.
'''

def print_nums(*args):
	if len(args) == 0:
		return ''
	args_arr = sorted(args)
	n = len(str(args_arr[-1]))
	ans = ''
	for i in args:
		if len(str(i)) < n:
			ans += '0'*(n-len(str(i))) + str(i)
			ans += '\\n'
		else:
			ans += str(i) + '\\n'
	return ans[0:len(ans)-2].replace('\\n', '\n')

print(print_nums(2,3,4,5,11,332))