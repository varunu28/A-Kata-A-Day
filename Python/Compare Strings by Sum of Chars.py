# Compare Strings by Sum of Chars
# Level: 7kyu
'''
Problem Description: Compare two strings by comparing the sum of their values (ASCII character code).
For comparing treat all letters as UpperCase.

Null-Strings should be treated as if they are empty strings.
If the string contains other characters than letters, treat the whole string as it would be empty.

Examples:

"AD","BC" -> equal

"AD","DD" -> not equal

"gf","FG" -> equal

"zz1","" -> equal

"ZzZz", "ffPFF" -> equal

"kl", "lz" -> not equal

null, "" -> equal

Your method should return true, if the strings are equal and fals if they are not equal.
'''

def compare(s1,s2):
    #your code here
    
    if (s1 is None and s2 is None) or (s1 is None and len(s2) == 0) or (len(s1) == 0 or s2 is None):
    	return True
    if (s1 is None and s2 is not None) or (s1 is not None and s2 is None):
    	return False
    if s1.isalpha() == False:
    	s1 = ''
    if s2.isalpha() == False:
    	s2 = ''

    sum1 = 0
    sum2 = 0

    for i in s1:
    	sum1 += ord(i.upper())

    for i in s2:
    	sum2 += ord(i.upper())

    return sum1 == sum2

# Test Cases

print(compare("AD", "BC"))
print(compare("AD", "DD"))
print(compare("gf", "FG"))
print(compare("Ad", "DD"))
print(compare("zz1", ""))
print(compare("ZzZz", "ffPFF"))
print(compare("kl", "lz"))
print(compare(None, ""))
print(compare("!!", "7476"))
print(compare("##", "1176"))


