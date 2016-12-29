# Recursive reverse string
# Level: 7kyu
'''
Problem Description: Your objective is to complete a recursive function reverse() that receives str as 
String and returns the same string in reverse order

Rules:

    reverse function should be executed only N times. N = length of the input string
    helper functions are not allowed
    changing the signature of the function is not allowed

Examples:

reverse("hello world") = "dlrow olleh" (N = 11)
reverse("abcd") = "dcba" (N = 4)
reverse("12345") = "54321" (N = 5)

All tests for this Kata are randomly generated, besides checking the reverse logic they will count how 
many times the reverse() function has been executed. 
'''

def reverse(str1):
	# your code here
	if len(str1) == 1:
		return str1
	else:
		return str1[-1] + reverse(str1[0:len(str1)-1])

# Test Cases

print(reverse("hello world"))
print(reverse("abcd"))
print(reverse("12345"))