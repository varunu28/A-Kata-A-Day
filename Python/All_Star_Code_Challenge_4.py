# All Star Code Challenge #4
# Level: Beta
'''
Create a function, called getCollege, that takes in an object of an nba player, and returns the 
college that the player went to
'''

def getCollege(player):
    return player['college']

# Test Case

curry = {'fname': "Steph", 'lname':"Curry", 'number':30, 'team':"Warriors", 'college':"Davidson"}
print(getCollege(curry))