# Simple Pig Latin
# Level: 5kyu
'''
Problem Description: Move the first letter of each word to the end of it, then add 'ay' to the end of 
the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''


def pig_it(text):
    text_arr = text.split(' ')
    ans = []
    for i in text_arr:
        if i[:-2] + i[:-1] != 'ay' and i[0].isalpha():
            temp = i[1:] + i[0] + 'ay'
            ans.append(temp)
        else:
            ans.append(i)
    return ' '.join(ans)

# Test Cases

print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
