# First non-repeating letter
# Level: 5kyu
'''
Problem Description: Write a function named firstNonRepeatingCharacter that takes a string input, and 
returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs 
once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function 
should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").
'''

def first_non_repeating_letter(string):
	low_str = []
	for i in string:
		low_str.append(i.lower())
	for i in string:
		if low_str.count(i.lower()) == 1:
			return i
	return ''

# Test Cases

print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('hello world, eh?'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))