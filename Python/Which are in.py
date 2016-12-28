# Which are in?
# Level : 6kyu
'''
Problem statement: Given two arrays of strings a1 and a2 return a sorted array r in lexicographical
order and without duplicates of the strings of a1 which are substrings of strings of a2.

Example 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]
Example 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
'''


def in_array(array1, array2):
    ans = []
    for i in array1:
        for j in array2:
            if i in j and i not in ans:
                ans.append(i)
                break
    ans.sort()
    return ans

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
