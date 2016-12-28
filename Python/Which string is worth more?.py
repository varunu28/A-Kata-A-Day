# Which string is worth more?
# Level: 7kyu
'''
Problem Description: You will be given two ASCII strings, a and b. Your task is write a function to 
determine which one of these strings is "worth" more, and return it.

A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string 
HELLO has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.

In the event of a tie, you should return the first string, i.e. a.
'''


def highest_value(a, b):
    # Write your solution
    a_score = 0
    b_score = 0
    for i in a:
        a_score += ord(i)
    for i in b:
        b_score += ord(i)
    if b_score > a_score:
        return b
    else:
        return a

print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))
