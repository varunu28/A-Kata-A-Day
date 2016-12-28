# Frequency sequence
# Level: Beta
'''
Problem Description: Return an output string that translates an input string s by replacing each 
character in s with a digit representing the number of times that character occurs in s and separating 
digits with the character(s) sep.
'''


def freq_seq(s, sep):
    ans = []
    for i in s:
        ans.append(str(s.count(i)))
    return sep.join(ans)

# Test Cases

print(freq_seq('hello world', '-'))
print(freq_seq('19999999',    ':'))
print(freq_seq('^^^**$',      'x'))
