def decode(string_):
    #your code here
    if type(string_) != type('gfd'):
    	return "Input is not a string"
    ans = ''
    inp = list('abcdefghijlkmnopqrstuvwxyz')
    for i in string_:
    	if i.isalpha():
    		if i.isupper():
    			ans += inp[::-1][inp.index(i.lower())].upper()
    			print(inp[::-1][inp.index(i.lower())].upper())
    		else:
    			ans += inp[::-1][inp.index(i)]
    			print(inp[::-1][inp.index(i)])
    	else:
    		ans += i 
    return ans


print(decode(("Blf zoivzwb szw 10 yvvih")))
#print(decode(12))