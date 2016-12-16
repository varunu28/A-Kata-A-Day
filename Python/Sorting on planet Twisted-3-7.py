# Sorting on planet Twisted-3-7
# Level: 6kyu
'''
Problem Description: There is a planet... in a galaxy far far away. It is exactly like our planet, but 
it has one difference:
The values of the digits 3 and 7 are twisted.

Our 3 means 7 on the planet Twisted-3-7. And 7 means 3.

Your task is to create a method, that can sort an array the way it would be sorted on Twisted-3-7.

7 Examples from a friend from Twisted-3-7:

[1,2,3,4,5,6,7,8,9] -> [1,2,7,4,5,6,3,8,9]
[12,13,14] -> [12,14,13]
[9,2,4,7,3] -> [2,7,4,3,9]

There is no need for a precheck. The array will always be not null and will always contain at least 
one number.

You should not modify the input array!
'''

# Swapping Value Function
def adj_arr(arr):
	new_arr = []
	i = 0
	while i < len(arr):
		j = 0
		str_i = list(str(arr[i]))
		while j < len(str_i):
			if str_i[j] == '7':
				str_i[j] = '3'
			elif str_i[j] == '3':
				str_i[j] = '7'
			j += 1
		new_arr.append(int(''.join(str_i)))
		i += 1
	return new_arr

def sort_twisted37(arr):
	return adj_arr(sorted(adj_arr(arr)))

# Test Cases

print(sort_twisted37([1,2,3,4,5,6,7,8,9]))
print(sort_twisted37([12,13,14]))
print(sort_twisted37([9,2,4,7,3]))