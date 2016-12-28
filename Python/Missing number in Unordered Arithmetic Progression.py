# Missing number in Unordered Arithmetic Progression
# Level: 5kyu
'''
Problem Description: And here is an unordered version. Try if you can survive lists of MASSIVE numbers
(which means time limit should be considered). :D

Note: Don't be afraid that the minimum or the maximum element in the list is missing, 
e.g. [4, 6, 3, 5, 2] is missing 1 or 7, but this case is excluded from the kata.

Example:

find([3, 9, 1, 11, 13, 5]) # => 7
'''


def find(seq):
    seq = sorted(seq)
    d = (seq[-1] - seq[0])//len(seq)
    i = 0
    while i < len(seq) - 1:
        if seq[i+1] - seq[i] != d:
            return seq[i] + d
        i += 1

# Test Cases

print(find([3, 9, 1, 11, 13, 5]))
print(find([5, -1, 0, 3, 4, -3, 2, -2]))
