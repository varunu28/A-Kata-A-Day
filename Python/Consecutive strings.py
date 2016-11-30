# Consecutive strings
# Level: 6kyu
'''
Problem Description: You are given an array strarr of strings and an integer k. Your task is to return 
the first longest string consisting of k consecutive strings taken in the array.
Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> 
"abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

'''

def longest_consec(strarr, k):
	ans = ''
	k -= 1
	l = 0
	i = 0
	while i < len(strarr) - k:
		temp_arr = list()
		j = 0
		while j <= k:
			temp_arr.append(strarr[i + j])
			j += 1

		temp = ''.join(temp_arr)
		if len(temp) > l:
			l = len(temp)
			ans = temp
		i += 1
	return ''.join(ans)

# Test Cases	

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", 
					  "oocccffuucccjjjkkkjyyyeehh"], 1))