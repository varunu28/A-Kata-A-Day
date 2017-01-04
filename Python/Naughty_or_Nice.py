# Naughty or Nice?
# Level: Beta
'''
In this kata, you will write a function that receives an array of string and returns a string that is 
either 'naughty' or 'nice'. Strings that start with the letters b, f, or k are naughty. Strings that 
start with the letters g, s, or n are nice. Other strings are neither naughty nor nice.

If there is an equal amount of bad and good actions, return 'naughty'
'''


def whatListAmIOn(actions):
    # Your code
    bad = 0
    good = 0
    for i in actions:
        if i[0] in ['b', 'f', 'k']:
            bad += 1
        elif i[0] in ['g', 's', 'n']:
            good += 1
    if good > bad:
        return 'nice'
    else:
        return 'naughty'

bad_actions = ['broke someone\'s window',
               'fought over a toaster', 'killed a bug']
good_actions = ['got someone a new car',
                'saved a man from drowning', 'never got into a fight']
actions = ['broke a vending machine',
           'never got into a fight', 'tied someone\'s shoes']

print(whatListAmIOn(bad_actions))
print(whatListAmIOn(good_actions))
print(whatListAmIOn(actions))
