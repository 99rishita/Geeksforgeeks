def neg_kadane(arr):
    sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        sum = max(arr[i], sum + arr[i])
        max_sum = max(max_sum, sum)

    return max_sum

arr = [-1,-2,-3,-4]
#arr = [-2, -3, 4, -1, -2, 1, 5, -3]
#arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
#arr = [1,-2,3,-2,5]
print(neg_kadane(arr))
