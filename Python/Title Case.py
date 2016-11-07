# Title Case
# Level : 6kyu
'''Problem Statement: A string is considered to be in title case if each word in the string is either (a) 
capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception 
and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space. Your function should 
ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
Arguments (Haskell)

    First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
    Second argument: the original string to be converted.

Arguments (Other languages)

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

'''

def title_case(title, minor_words=''):
	title_arr = title.split(' ')
	minor_arr = minor_words.split(' ')
	i = 0
	while i < len(minor_arr):
		minor_arr[i] = minor_arr[i].lower()
		i += 1

	i = 0
	while i < len(title_arr):
		if title_arr[i].lower() not in minor_arr:
			title_arr[i] = title_arr[i].title()
		else:
			if i == 0:
				title_arr[i] = title_arr[i].title()
			else:
				title_arr[i] = title_arr[i].lower()
		i += 1
	return " ".join(title_arr)

