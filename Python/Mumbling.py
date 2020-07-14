# Mumbling
# Level: 7kyu
'''
This time no story, no theory. The examples below show you how to write function accum:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
'''

def accum(s):
    # your code
    ans = ''
    for i in range(len(s)):
    	for n in range(i+1):
    		if n == 0:
    			ans += s[i].upper()
    		else:
    			ans += s[i].lower()
    	ans += '-'
    return ans[:len(ans)-1]

