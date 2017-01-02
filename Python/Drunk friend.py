# Drunk friend
# Level: 6kyu
'''
Problem Description: You're hanging out with your friends in a bar, when suddenly one of them is so drunk, that he can't
speak, and when he wants to say something, he writes it down on a paper. However, none of the words he writes make sense
to you. He wants to help you, so he points at a beer and writes "yvvi". You start to understand what he's trying to say,
and you write a script, that decodes his words.

Keep in mind that numbers, as well as other characters, can be part of the input, and you should keep them like they are.
You should also test if the input is a string. If it is not, return "Input is not a string".
'''

def decode(string_):
    #your code here
    if type(string_) != type('gfd'):
    	return "Input is not a string"
    ans = ''
    inp = []
    for j in range(65,91):
        inp.append(chr(j))
    for i in string_:
    	if i.isalpha():
    		if i.isupper():
    			ans += inp[::-1][inp.index(i)]
    		else:
    			ans += inp[::-1][inp.index(i.upper())].lower()
    	else:
    		ans += i 
    return ans


print(decode(("Blf zoivzwb szw 10 yvvih")))
print(decode(12))
