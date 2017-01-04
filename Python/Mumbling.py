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
    i = 0
    while i < len(s):
    	n = 0
    	while n < i+1:
    		if n == 0:
    			ans += s[i].upper()
    		else:
    			ans += s[i].lower()
    		n += 1
    	ans += '-'
    	i += 1
    return ans[:len(ans)-1]

