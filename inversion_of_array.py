def inversion(arr):
    n = len(arr)
    count = 0
    i = 0
    j = n-1
    while(n>0):
        if j == i:
            i += 1
            n = len(arr)-i
            j = len(arr)-1
            continue
        if arr[i]>arr[j]:
            count += 1
        j -= 1
        n -= 1
    return count

#arr = [2,4,1,3,5]
#arr = [8,4,2,1]
arr = [1, 20, 6, 4, 5]
print(inversion(arr))