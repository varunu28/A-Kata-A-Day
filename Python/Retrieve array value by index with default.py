# Retrieve array value by index with default
# Level: 7kyu
'''
Problem Description: Complete the solution. It should try to retrieve the value of the array at the 
index provided. If the index is out of the array's max bounds then it should return the default value 
instead. 
'''

def solution(items, index, default_value):
    if index >= 0 and index < len(items):
    	return items[index]
    if index < 0:
    	if abs(index) <= len(items):
    		return items[index]
    return default_value

# Test Cases

rng = list(range(1, 4))
print(solution(rng, 1, 'a'))
print(solution(rng, -1, 'a'))
print(solution(rng, -5, 'a'))
print(solution(rng, -3, 'a'))