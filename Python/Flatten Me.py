# Flatten Me
# Level: 7kyu
'''
In this kata, your task is to create a function that takes a single list as an argument and returns a 
flattened list. The input list will have a maximum of one level of nesting (list(s) inside of a list).
'''

def flatten_me(lst):
	ans = []
	for i in lst:
		if type(i) is list:
			for j in i:
				ans.append(j)
		else:
			ans.append(i)
	return ans

print(flatten_me([1, [2, 3], 4]))