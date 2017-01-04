# Is every value in the array an array?
# Level : 7kyu
'''
Problem Description: Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have 
to be arrays.

Examples:

[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
'''


def arr_check(arr):
    for i in arr:
        if isinstance(i, list) == False:
            return False
    return True

# Test Case

print(arr_check([]))
print(arr_check([['string']]))
print(arr_check([[], {}]))
print(arr_check([[1], [2], [3]]))
print(arr_check(["A", "R", "R", "A", "Y"]))
