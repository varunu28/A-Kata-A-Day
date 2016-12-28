# List Filtering
# Level: 7kyu
'''
Problem Description: In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.
'''


def filter_list(l):
    ans = []
    for i in l:
        if isinstance(i, int):
            ans.append(i)
    return ans

print(filter_list([1, 2, 'a', 'b']))
