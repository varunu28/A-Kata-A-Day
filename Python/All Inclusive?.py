# All Inclusive?
# Level: 7kyu
'''
Input:

    a string strng
    an array of strings arr

Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

    a boolean true if all rotations of strng are included in arr (C returns 1)
    false otherwise (C returns 0)
'''


def rotate(l, n):
    return l[n:] + l[:n]


def contain_all_rots(strng, arr):
    if len(strng) == 0:
        return True
    i = 0
    while i < len(strng):
        if ''join(rotate(list(strng), i)) not in arr:
            return False
        i += 1
    return True


print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
