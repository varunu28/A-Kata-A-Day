# All Star Code Challenge #1
# Level: Beta
'''
Problem Description: Write a function, called sumPPG, that takes two NBA player objects and sums their 
PPG

-- Player is defined as:
data Player = Player { team :: String, ppg :: Double } deriving (Show)
'''

def sum_ppg(playerOne, playerTwo):
    # Your code here
    return playerOne['ppg'] + playerTwo['ppg']

# Test Case

iverson = { 'team': '76ers', 'ppg': 11.2 }
jordan  = { 'team': 'bulls', 'ppg': 20.2 }

print(sum_ppg(iverson, jordan))