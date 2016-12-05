# Crazed Templating
# Level: 6kyu
'''
Problem Description: Your crazy uncle has found a new hobby - he will occasionally scream out random 
words of the same length. Since he was a renowned Computer Scientist, you think he must have some 
pattern to this craziness. The words seem to always have a few letters in the same place, so maybe if 
you find his pattern his new amusement will stop annoying you.

Your task then, is to design a function letter_pattern that takes in a list of strings (all lowercase,
and only including letters). It should return a string with every letter that is always there in 
place.
Example

['war', 'rad', 'dad'] should return "*a*", since only the second place stays constant

['general', 'admiral', 'piglets', 'secrets'] should return "*******"

['family'] should return "family"
'''

def letter_pattern(words):
	if len(words) == 1:
		return words[0]
	else:
		ans = []
		i = 0
		while i < len(words[0]):
			sample = words[0][i]

			j = 1
			c = 1

			while j < len(words):
				if sample != words[j][i]:
					c = 0
					ans.append('*')
					break
				j += 1

			if c:
				ans.append(sample)

			i += 1
		return ''.join(ans)

# Test Cases

test_list = ['war', 'rad', 'dad']
print(letter_pattern(test_list))

test_list = ['general', 'admiral', 'piglets', 'secrets']
print(letter_pattern(test_list))

test_list = ['family']
print(letter_pattern(test_list))