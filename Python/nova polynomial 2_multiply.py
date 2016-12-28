# Nova polynomial Multiply
# Level: 6kyu
'''
Problem Description: This kata is from a series on polynomial handling. ( #1 #2 #3 #4)

Consider a polynomial in a list where each element in the list element corresponds to the factors. The 
factor order is the position in the list. The first element is the zero order factor (the constant).

p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

In this kata multiply two polynomials:

poly_multiply([1, 2], [1] ) = [1, 2]
poly_multiply([2, 4], [4, 5] ) = [8, 26, 20]
'''


def poly_multiply(p1, p2):
    res = [0]*(len(p1)+len(p2)-1)
    for o1, i1 in enumerate(p1):
        for o2, i2 in enumerate(p2):
            res[o1+o2] += i1*i2
    if res.count(0) == len(res):
        return []
    else:
        return res

# Test Case

print(poly_multiply([1, 2], [2]))
print(poly_multiply([2, 4], [4, 5]))
