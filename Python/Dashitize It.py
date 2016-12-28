# Dasitize It
# Level : 6kyu
'''
Problem Description:
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the 
string with a dash mark.
'''


def dashatize(num):
    if num is None:
        return "None"

    if num < 0:
        num *= -1

    str_num = str(num)

    if len(str_num) == 1:
        return str_num

    i = 0
    ans = []
    while i < len(str_num):
        if i == 0:
            ans.append(str_num[i])
            if int(str_num[i]) % 2 != 0 and int(str_num[i+1]) % 2 == 0:
                ans.append('-')
        elif i == len(str_num) - 1:
            if int(str_num[i]) % 2 != 0:
                ans.append('-')
            ans.append(str_num[i])
        else:
            if int(str_num[i]) % 2 != 0:
                ans.append('-')
            ans.append(str_num[i])
            if int(str_num[i]) % 2 != 0:
                if int(str_num[i+1]) % 2 == 0:
                    ans.append('-')
        i += 1
    return ''.join(ans)


# Test Cases

print(dashatize(974302))
print(dashatize(86320))
print(dashatize(5311))
print(dashatize(274))
print(dashatize(0))
print(dashatize(-1))
print(dashatize(-28369))
print(dashatize(None))
print(dashatize(18215031))
