# Vowel Count
# Level: 7kyu
'''
Problem Description: Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
'''

def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    # your code here
    for i in inputStr:
        if i in vowels:
            num_vowels += 1

    return num_vowels


print(getCount("abracadabra"))