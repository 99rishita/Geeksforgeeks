def missing_num(arr, n):
    map = {}
    for i in range(0, len(arr)):
        map[arr[i]] = i
    for i in range(1, n+1):
        if i not in map:
            return i


#arr = [1,2,3,5]
#n = 10
#arr = [1,2,3,4,5,6,7,8,10]
arr = [1, 2, 4, 6, 8, 7, 5]
n = 8
print(missing_num(arr, n))