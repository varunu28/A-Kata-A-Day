# Sum up the random string
# Level: 7kyu
'''
Problem Description: Given a random string consisting of numbers, letters, symbols, you need to sum up 
the numbers in the string.

Note:

    Consecutive integers should be treated as a single number. eg, 2015 should be treated as a single 
    number 2015, NOT four numbers
    All the numbers should be treaded as positive integer. eg, 11-14 should be treated as two numbers 11 
    and 14. Same as 3.14, should be treated as two numbers 3 and 14
    If no number was given in the string, it should return 0

Example:

str = "In 2015, I want to know how much does iPhone 6+ cost?"

The numbers are 2015, 6

Sum is 2021.
'''

def sum_from_string(string):
	s = 0
	i = 0
	n1 = ''
	while i < len(string):
		if string[i].isdigit():
			n1 += string[i]
		else:
			if len(n1) > 0:
				s += int(n1)
				n1 = ''
		i += 1
		if i == len(string):
			if len(n1) > 0:
				s += int(n1)
				n1 = ''
	return s 

# Test Cases

print(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"))
print(sum_from_string("1+1=2"))