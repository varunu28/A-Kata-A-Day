# Where my anagrams at?
# Level: 5kyu
'''
Problem Description: What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. 
'''

def anagrams(word, words):
	word_arr = sorted(list(word))
	ans = []
	for i in words:
		if sorted(list(i)) ==  word_arr:
			ans.append(i)
	return ans

# Test Cases

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

