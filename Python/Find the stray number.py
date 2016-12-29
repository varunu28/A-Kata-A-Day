# Find the stray number
# Level: 7kyu
'''
Problem Description: You are given an odd-length array of integers, in which all of them are the same, 
except for one single number.

Implement the method stray which accepts such array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)
'''

def stray(arr):
	arr_set = set(arr)
	for i in arr_set:
		if arr.count(i) == 1:
			return i

# Test Cases

print(stray([1,1,1,1,1,1,2]))
print(stray([2,3,2,2,2]))
print(stray([3,2,2,2,2]))