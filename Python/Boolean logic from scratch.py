# Boolean logic from scratch
# Level: 7kyu
'''
Problem Description: You need to implement two functions, xor and or, that replicate the behaviour of 
their respective operators:

    xor = Takes 2 values and returns true if, and only if, one of them is truthy.
    or = Takes 2 values and returns true if either one of them is truthy.

When doing so, you cannot use the or operator:
||
.
Input

    Not all input will be booleans - there will be truthy and falsey values
    There will always be 2 values provided

Examples

    xor(true, true) should return false
    xor(false, true) should return true
    or(true, false) should return true
    or(false, false) should return false
'''

def func_or(a,b):
    #your code here - do no be lame and do not use built-in code!
    if a or b:
    	return True
    else:
    	return False 

def func_xor(a,b):
    #your code here - remember to consider truthy and falsey value 
    if (a and bool(b) == False) or (bool(a) == False and b):
    	return True
    else:
    	return False

# Test Cases

print(func_or(0, 11))
print(func_xor(True, True))