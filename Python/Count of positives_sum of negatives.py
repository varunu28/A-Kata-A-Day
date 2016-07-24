#Count of positives / sum of negatives
#Level: 8kyu
'''
Problem Statement: Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element is sum of negative
numbers.
'''

def count_positives_sum_negatives(arr):
    count_pos = 0
    sum_neg = 0
    for i in arr:
        if i > 0:
            count_pos+=1
        else:
            sum_neg += i
    ans = []
    ans.append(count_pos)
    ans.append(sum_neg)
    return ans
    


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(arr))


