# Pairing brackets
# Level: 6kyu
'''
Problem Description: Write a function which outputs the positions of matching bracket pairs. The 
output should be a dictionary with keys the positions of the open brackets '(' and values the 
corresponding positions of the closing brackets ')'.

For example: input = "(first)and(second)" should return {0:6, 10:17}

If brackets cannot be paired or if the order is invalid (e.g. ')(') return False. In this kata we care 
only about the positions of round brackets '()', other types of brackets should be ignored.
'''

def bracket_pairs(string):
    #return a dictionary with open/close position pairs
    if string.count('(') != string.count(')'):
    	return False
    ans = dict()
    stack = []
    i = 0
    while i < len(string):
    	if string[i] == '(':
    		stack.append(i)
    	if string[i] == ')':
    		if len(stack) == 0:
    			return False
    		else:
    			ans[stack[-1]] = i
    			del stack[-1]
    	i += 1
    return ans

# Test Cases

print(bracket_pairs("len(list)"))
print(bracket_pairs("def f(x"))
print(bracket_pairs("(a(b)c()d)"))