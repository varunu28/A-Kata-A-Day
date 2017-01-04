# Rectangle into Squares
# Level: 6kyu
'''
Problem Description: The drawing below gives an idea of how to cut a given "true" rectangle into squares 
("true" rectangle meaning that the two dimensions are different).

alternative text

Can you translate this drawing into an algorithm?

You will be given two dimensions

    a positive integer length (parameter named lng)
    a positive integer width (parameter named wdth)

You will return an array with the size of each of the squares.

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
'''


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    ans = []
    while lng != wdth:
        if lng > wdth:
            lng -= wdth
            ans.append(wdth)
        elif wdth > lng:
            wdth -= lng
            ans.append(lng)

    ans.append(lng)
    return ans

# Test Cases

print(sqInRect(5, 5))
print(sqInRect(5, 3))
print(sqInRect(3, 5))
