# Calculate mean and concatenate string
# Level: 7kyu
'''
Problem Description: You will be given an array of strings which will include both integers and 
characters.

Return an array of length 2 with a[0] representing the mean of the integers to a single decimal place. 
There will always be 10 integers and 10 characters. Create a single string with the characters and 
return it as a[1] while maintaining the original order.
'''

def mean(lst):
	s = 0
	c = 0
	str1 = ''
	for i in lst:
		if ord(i) >= 65 and ord(i) <= 122:
			str1 += i
		else:
			s += int(i)
			c += 1
	mean = 0
	if c > 0:
		mean = float(s)/float(c) 
	return [mean, str1]

lst = lst1 = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
print(mean(lst))

    