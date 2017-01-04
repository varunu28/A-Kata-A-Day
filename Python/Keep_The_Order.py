# Keep the Order
# Level: 7 kyu
'''
Problem Description:
Your job here is to write a function (keepOrder in JS/CoffeeScript,
keep_order in Ruby/Crystal/Python), which takes a sorted array ary and a
value val, and returns the lowest index where you could insert val to
maintain the sorted-ness of the array. The input array will always be sorted
in ascending order. It may contain duplicates.

Do not modify the input.
Some examples:

keep_order([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)
'''


def keep_order(ary, val):
    i = 0
    while i < len(ary):
        if ary[i] >= val:
            break
                i += 1
    return i
print(keep_order([1, 2, 3, 4, 7], 5))
print(keep_order([1, 2, 3, 4, 7], 0))
print(keep_order([1, 1, 2, 2, 2], 2))
