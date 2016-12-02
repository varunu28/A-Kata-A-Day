# Largest 5 digit number in a series
# Level: 5kyu
'''
Problem Description: In the following 6 digit number:

283910

91 is the greatest sequence of 2 digits.

Complete the solution so that it returns the largest five digit number found within the number given.. The number will be passed in 
as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 
digits. 
'''

def solution(digits):
    large = 0
    i = 0
    while i < len(digits) - 4:
    	if int(digits[i:i+5]) > large:
    		large = int(digits[i:i+5])
    	i += 1
    return large

# Test Case

print(solution('1234567898765'))