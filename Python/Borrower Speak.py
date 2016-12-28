# Borrower Speak
# Level: 7kyu
'''
Problem Description: The borrowers are tiny tiny fictional people. As tiny tiny people they have to be 
sure they aren't spotted, or more importantly, stepped on.

As a result, the borrowers talk very very quietly. They find that capitals and punctuation of any sort 
lead them to raise their voices and put them in danger.

The young borrowers have begged their parents to stop using caps and punctuation.

Change the input text 's' to new borrower speak. Help save the next generation!
'''


def borrow(s):
    alp_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = list(s)
    ans_s = list()

    for i in s:
        if i.lower() in alp_arr:
            ans_s.append(i.lower())
    return ''.join(ans_s)

# Test Cases

print(borrow('WhAt! FiCK! DaMn CAke?'))
print(borrow('THE big PeOpLE Here!!'))
