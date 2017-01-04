# Thinkful - String Drills: Areacode extractor
# Level: 7kyu
'''
Problem Description: You've got a bunch of textual data with embedded phone numbers. Write a function 
area_code() that finds and returns just the area code portion of the phone number.

>>> message = "The supplier's phone number is (555) 867-5309"
>>> area_code(message)
'555'

The returned area code should be a string, not a number. Every phone number is formatted like in the 
example, and the only non-alphanumeric characters in the string are apostrophes ' or the punctuation 
used in the phone number.
'''

def area_code(text):
    # Your code goes here
    return text[text.index('(')+1:text.index(')')]

# Test Cases

print(area_code("The supplier's phone number is (555) 867-5309"))
print(area_code("Grae's cell number used to be (123) 456-7890"))
print(area_code("The 102nd district court's fax line is (124) 816-3264"))