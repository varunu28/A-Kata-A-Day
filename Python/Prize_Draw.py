# Prize Draw
# Level: 6kyu
'''
Problem Description: To participate in a prize draw each one gives his/her firstname.

Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so
on.

The length of the firstname is added to the sum of these ranks hence a number n. An array of random weights is linked to the
firstnames and each n is multiplied by its corresponding weight to get what they call a winning number.

Example: names: COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH weights: [1, 4, 4, 5, 2, 1]

PAUL -> n = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54 The weight associated with PAUL is 2 so Paul's winning 
number is 54 * 2 = 108.

Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.

Task:

parameters: st a string of firstnames, we an array of weights, n a rank

return: the firstname of the participant whose rank is n (ranks are numbered from 1)
Example:

names: COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH weights: [1, 4, 4, 5, 2, 1] n: 4

The function should return: PauL
Note:

If st is empty return "No participants".

If n is greater than the number of participants then return "Not enough participants".
'''


def rank(st, we, n):
    d = dict()
    if len(st) == 0:
        return "No participants"
    st = st.split(',')
    k = 0

    for i in st:
        s = 0
        for j in i:
            s += ord(j.lower()) - 97 + 1
        s += len(i)
        d[i] = s*we[k]
        k += 1
    d = sorted(sorted(d), key=d.get, reverse=True)

    if len(d) < n:
        return "Not enough participants"
    else:
        return d[n-1]

# Test Case

print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
           [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Lagon,Lily", [1, 5], 2))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
           [4, 2, 1, 4, 3, 1, 2], 8))
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))
