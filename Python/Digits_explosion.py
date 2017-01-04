# Digits explosion
# Level: 7kyu
'''
Problem Description: Given a string made of digits [0-9] returns a string where each digit is repeated 
a number of times equals to its value. 
'''


def explode(s):
    ans = ''
    for i in s:
        ans += i*int(i)
    return ans

# Test Cases

s = "312"
print(explode(s))

s = "102269"
print(explode(s))
