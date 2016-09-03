#Sum the Repeats
#Level: 7kyu
'''
Problem Statement: Write a function that takes a list comprised of other lists of integers and 
returns the sum of all numbers that appear in two or more lists in the input list. Now that might 
have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
'''

def repeat_sum(l):
    
    if len(l) <= 1:
    	return 0

    temp_full =[]
    for temp in l:
    	mid = []
    	for i in temp:
    		if i not in mid:
    			mid.append(i)
    	temp_full.append(mid)
    
    full = []
    for i in temp_full:
    	for j in i:
    		full.append(j)

    sum_arr = []
    for j in full:
    	if full.count(j) > 1 and j not in sum_arr:
    		sum_arr.append(j)

    return sum(sum_arr)

print(repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])) 
