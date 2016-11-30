# Numbers to Letters
# Level: 7kyu
'''
Problem Description: Given an array of numbers, you must return a string. The numbers correspond to the 
letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' ' 
that are represented by '27', '28' and '29' respectively.

All inputs will be valid.

'''

def switcher(arr):
	alp_arr = [' ', '?', '!', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
			   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	num_arr = [str(i) for i in range(1,30)][::-1]
	ans = []

	for i in arr:
		if i in num_arr:
			ans.append(alp_arr[num_arr.index(i)])
	return ''.join(ans)

# Test Case

print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))
print(switcher(['25','7','8','0','4','14','23','8','25','23','29','16','16','4']))