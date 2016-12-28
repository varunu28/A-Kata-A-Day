# Write Number in Expanded Form
# Level: 6kyu
'''
Problem Description: You will be given a number and you will need to return it as a string in Expanded 
Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''


def expanded_form(num):
    i = 10**(len(str(num))-1)
    ans = ''
    while num:
        if (num//i)*i != 0:
            ans += str((num//i)*i) + ' + '
        num = num % i
        i //= 10
    return (ans[0:len(ans)-3])

# Test Cases

print(expanded_form(42))
print(expanded_form(12))
print(expanded_form(70304))
