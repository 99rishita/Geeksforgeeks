def binary_searching(findnumber, arr, start, end):
    if end >= start:
        mid = start + (end-start) // 2
        if arr[mid] == findnumber:
            return arr[mid]
        elif arr[mid] < findnumber:
            return binary_searching(findnumber, arr, mid+1, end)
        else:
            return binary_searching(findnumber, arr, start, mid-1)
    else:
        return -1

arr = [10,20,30,40,50,60,70,80,90,100,110]
findnumber = 110
print(binary_searching(findnumber, arr, 0, len(arr)-1))
    