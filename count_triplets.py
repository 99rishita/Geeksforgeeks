def count_triples(arr):
    map = {}
    sum = 0
    count = 0
    for i in range(0, len(arr)):
        map[arr[i]] = i
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            sum = arr[i] + arr[j]
            if sum in map:
                count += 1
    if count == 0:
        return -1
    else:
        return count
arr = [1,2,3,4,5]
print(count_triples(arr))