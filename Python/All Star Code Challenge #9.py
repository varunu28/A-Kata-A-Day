# All Star Code Challenge #9
# Level: Beta
'''
Problem Description: This Kata is intended as a small challenge for my students

Create a function named bite(), that takes a human object as input and convert its "race" to a "zombie" 
and returning the object

Note: If the object does NOT contain a "race" key, the return object should NOT be changed in any way
'''

def bite(thing):
    # Your code here
    if 'race' in thing:
    	thing['race'] = 'zombie'
    return thing

print(bite({'race':'human'}))