# Nova polynomial add
# Level : Beta
'''
Problem Description: Consider a polynomial in a list where each element in the list element corresponds to
the factors. The factor order is the position in the list. The first element is the zero order factor 
(the constant).

p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

In this kata add two polynomials:

poly_add ( [1, 2], [1] ) = [2, 2]
'''

# return the sum of the two polynomials p1 and p2.


def poly_add(p1, p2):
    l1 = len(p1)
    l2 = len(p2)
    m = min(l1, l2)
    ans = []
    i = 0
    while i < m:
        ans.append(p1[i] + p2[i])
        i += 1
    if m == l1:
        while i < l2:
            ans.append(p2[i])
            i += 1
    else:
        while i < l1:
            ans.append(p1[i])
            i += 1
    return ans

# Test Case

print(poly_add([1], [1]))
print(poly_add([1, 2], [1]))
