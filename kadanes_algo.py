import sys
def kadane(arr):
    max_sum = -sys.maxsize - 1
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
        if max_sum < sum:
            max_sum = sum
    return max_sum

#arr = [-1,-2,-3,-4]
#arr = [-2, -3, 4, -1, -2, 1, 5, -3]
#arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
arr = [1,-2,3,-2,5]
print(kadane(arr))

