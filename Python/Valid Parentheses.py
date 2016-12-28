# Valid Parentheses
# Level: 6kyu
'''
Problem Description: Write a function called validParentheses that takes a string of parentheses, and determines 
if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false 
if it's invalid.

Examples:
validParentheses( "()" ) => returns true
validParentheses( ")(()))" ) => returns false
validParentheses( "(" ) => returns false
validParentheses( "(())((()())())" ) => returns true

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
'''


def valid_parentheses(string):
    brac = 0
    for i in string:
        if i == '(':
            brac += 1
        elif i == ')':
            brac -= 1
        if brac < 0:
            return False
    if brac != 0:
        return False
    else:
        return True

# Test Cases

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
