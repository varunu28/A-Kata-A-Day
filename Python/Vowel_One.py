# Vowel one
# Level: 7 kyu
'''
Problem Description: Write a function that takes a string and outputs a strings of 1's and 0's where 
vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.
'''


def vowel_one(s):
    ans = []
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in vow:
            ans.append('1')
        else:
            ans.append('0')
    return ''.join(ans)

# Test Cases

print(vowel_one("vowelOne"))
print(vowel_one("123, arou"))
print(vowel_one("Codewars"))
print(vowel_one("Python"))
