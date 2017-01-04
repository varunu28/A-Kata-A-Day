# All Star Code Challenge #6
# Level: Beta
'''
After watching the movie "Arrival", your friend Hannah is obsessed with palindrome names. She wants a quick way to check if anyone she knows has one of these unique names.

Create a function, called isPalindrome, that checks if a string is the same backwards as forwards, returning true or false accordingly.

If a non-string value is given as an argument, the function should throw an error.

isPalindrome("Hannah") // => true
isPalindrome("Billy") // => false 
isPalindrome(1) // => Error
'''

def isPalindrome(string):
	return string.lower() == string.lower()[::-1]

