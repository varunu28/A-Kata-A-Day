# Averages of numbers
# Level: 7kyu
'''
Problem Description: Write a method, that gets an array of integer-numbers and return an array of the 
averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]

If the array has 0 or 1 values or is null or None, your method should return an empty array.

Have fun coding it and please don't forget to vote and rank this kata! :-)
'''

def averages(arr):
	if arr is None:
		return []
	if len(arr) <= 1:
		return []
	ans = []
	i = 0
	while i < len(arr) - 1:
		ans.append((arr[i] + arr[i+1])/2)
		i += 1
	return ans

print(averages([1, 3, 5, 1, -10]))