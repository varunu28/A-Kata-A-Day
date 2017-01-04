# Counting Duplicates
# Level: 6kyu
'''
Problem Description: Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the input string. The input 
string can be assumed to contain only alphanumeric characters, including digits, uppercase and 
lowercase alphabets. 
'''

def duplicate_count(text):
    # Your code goes here
    text_set = set(list(text.lower()))
    count = 0
    for i in text_set:
    	if text.lower().count(i) > 1:
    		count += 1
    return count

# Test Cases

print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))