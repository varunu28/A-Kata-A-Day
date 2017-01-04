# Don't Drink the Water
# Level: 5kyu
'''
Problem Description: Given a two-dimensional array representation of a glass of mixed liquids, sort 
the array such that the liquids appear in the glass based on their density. (Lower density floats to 
the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]
'''


def separate_liquids(glass):
    if len(glass) == 0:
        return []
    d = {'H': 1.36, 'W': 1.00, 'A': 0.87, 'O': 0.80}
    d_rev = {1.36: 'H', 1.00: 'W', 0.87: 'A', 0.80: 'O'}
    flat_glass = []
    for i in glass:
        for j in i:
            flat_glass.append(d[j])
    flat_glass = sorted(flat_glass)

    n = len(glass[0])
    i = 0
    ans = []
    temp = []
    for k in flat_glass:
        temp.append(d_rev[k])
        i += 1
        if i == n:
            ans.append(temp)
            i = 0
            temp = []
    return ans

print(separate_liquids([['A', 'A', 'O', 'H'], ['A', 'H', 'W', 'O'], [
      'W', 'W', 'A', 'W'], ['H', 'H', 'O', 'O']]))
