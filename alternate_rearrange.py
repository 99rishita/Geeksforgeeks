def alternate(arr):
    max_ele = arr[len(arr)-1]
    min_ele = arr[0]
    for i in range(0, len(arr)):
        if i%2 == 0:
            arr[i] = max_ele
            max_ele -= 1
        if i%2 == 1:
            arr[i] = min_ele
            min_ele += 1

    return arr

#arr = [1,2,3,4,5,6,7,8,9]
arr = [1,2,3,4,5,6,7,8]
print(alternate(arr))
