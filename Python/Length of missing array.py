# Length of missing array
# Level: 6kyu
'''
Problem Description: You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3


If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays. 
'''

def get_length_of_missing_array(array_of_arrays):
    if array_of_arrays is None:
    	return 0
    elif len(array_of_arrays) == 0:
    	return 0
    else:
    	for i in array_of_arrays:
    		if i is None or len(i) == 0:
    			return 0

    len_arr = []
    for i in array_of_arrays:
    	len_arr.append(len(i))
    len_arr = sorted(len_arr)
    i = 0
    while i < len(len_arr)-1:
    	if len_arr[i+1] - len_arr[i] > 1:
    		return len_arr[i] + 1
    	i += 1

# Test Cases

print(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
print(get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
print(get_length_of_missing_array([[None], [None, None, None]]))
print(get_length_of_missing_array([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], 
								  ['a', 'a', 'a', 'a','a', 'a']]))