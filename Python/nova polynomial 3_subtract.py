# Nova polynomial subtract
# Level: 7kyu
'''
Problem Description: Consider a polynomial in a list where each element in the list element corresponds to the factors. 
The factor order is the position in the list. The first element is the zero order factor (the constant).

p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

In this kata subtract two polynomials:

poly_subtract([1, 2], [1] ) = [0, 2]
poly_subtract([2, 4], [4, 5] ) = [-2, -1]
'''

# return the subtraction of the two polynomials p1 and p2.  
def poly_subtract(p1, p2):
	if len(p1) == 0:
		return [-1*i for i in p2]
	if len(p2) == 0:
		return p1
	l1 = len(p1)
	l2 = len(p2)
	m = min(l1,l2)
	ans = []
	i = 0
	while i < m:
		ans.append(p1[i] - p2[i])
		i += 1
	if m == l1:
		while i < l2:
			ans.append(-1*p2[i])
			i += 1
	else:
		while i < l1:
			ans.append(p1[i])
			i += 1
	return ans

# Test Cases

print(poly_subtract([1],[1]))
print(poly_subtract([], [1,2,3,4,5,6]))
print(poly_subtract([1,2,3,4,5,6], []))