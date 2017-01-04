# Friend or Foe?
# Level: 7kyu
'''
Problem Description: Make a program that filters a list of strings and returns a list with only your friends name in 
it.

If a name has 4 letters in it, you can be sure that it has to be a friend of yours!

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

'''


def friend(x):
    ans = []
    for i in x:
        if len(i) == 4:
            ans.append(i)

    return ans

# Test Case
print(friend(["Ryan", "Kieran", "Mark", ]))
