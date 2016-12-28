# String Reversing, Changing case, etc.
# Level: 7kyu
'''
Problem Description: 
Given 2 string parameters, show a concatenation of:

    the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
    a separator in between both strings: @@@
    1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER
'''


def reverseAndMirror(s1, s2):
    ans_1 = ''.join(c.lower() if c.isupper() else c.upper() for c in s2)[::-1]
    ans_2_1 = ''.join(c.lower() if c.isupper() else c.upper()
                      for c in s1)[::-1]
    ans_2_2 = ''.join(c.lower() if c.isupper() else c.upper() for c in s1)
    return ans_1 + '@@@' + ans_2_1 + ans_2_2

s1, s2 = "FizZ", "buZZ"
print(reverseAndMirror(s1, s2))
