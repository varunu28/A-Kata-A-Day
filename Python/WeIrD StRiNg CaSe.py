# WeIrD StRiNg CaSe
# Level: 6kyu
'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string 
with all even indexed characters in each word upper cased, and all odd indexed characters in each word 
lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that 
character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only 
be present if there are multiple words. Words will be separated by a single space(' ').
'''


def to_weird_case(string):
    ans = []
    string = string.split()
    for j in string:
        i = 0
        temp = ''
        while i < len(j):
            if i % 2 == 0:
                temp += j[i].upper()
            else:
                temp += j[i].lower()
            i += 1
        ans.append(temp)
    return ' '.join(ans)

print(to_weird_case('This is a test'))
