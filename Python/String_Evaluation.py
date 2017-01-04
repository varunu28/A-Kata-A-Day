# String Evaluation
# Beta
'''
Problem Description: evaluate a string to determine if it passes certain conditons

The string will be as such:

"aab#HcCcc##l#"

The conditions will be passed in an array as such:

["a<b","#==4","c>=C","H!=a"]

The conditions in this example array can be interpreted as:

1) (a<b):The number of times 'a' occurs in the string should be less than the number of times 'b' occurs in the 
string

2) (#==4):'#' should occur 4 times in the string

3) (c>=C):'c' should occur greater than or equal to the number of times 'C' occurs.

4) (P!=a): The number of times 'P' occurs should not equal the number of times 'a' occurs

In this example condition 1 is false and 2,3,4 are true. So the return value will be an array as such:

[False,True,True,True]

Characters in conditions will always be in the string. Characters in the string are chosen from:

string.ascii_letters+"@#$%^&*()_{}[]"
'''


def string_evaluation(strng, conditions):
    ans = []
    for i in conditions:
        if '==' in i:
            temp = i.split('==')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) == int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) == int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) == strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) == strng.count(temp[1]))
        elif '!=' in i:
            temp = i.split('!=')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) != int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) != int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) != strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) != strng.count(temp[1]))
        elif '>=' in i:
            temp = i.split('>=')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) >= int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) >= int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) >= strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) >= strng.count(temp[1]))
        elif '<=' in i:
            temp = i.split('<=')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) <= int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) <= int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) <= strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) <= strng.count(temp[1]))
        elif '>' in i:
            temp = i.split('>')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) > int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) > int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) > strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) > strng.count(temp[1]))
        elif '<' in i:
            temp = i.split('<')
            if temp[1].isnumeric() and temp[0].isnumeric():
                ans.append(int(temp[0]) < int(temp[1]))
            elif temp[1].isnumeric():
                ans.append(strng.count(temp[0]) < int(temp[1]))
            elif temp[0].isnumeric():
                ans.append(int(temp[0]) < strng.count(temp[1]))
            else:
                ans.append(strng.count(temp[0]) < strng.count(temp[1]))

    return ans

# Test Cases

print(string_evaluation('aab#HcCcc##l#', ['a<b', '#==4', 'c>=C', 'H!=a']))
print(string_evaluation('abc#$%KDAyyaa@@@', ['#>@', 'A==2', 'a>A', '$!=2']))
print(string_evaluation(
    'abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']))
print(string_evaluation(
    'abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1', '2==2', '5>=4']))
