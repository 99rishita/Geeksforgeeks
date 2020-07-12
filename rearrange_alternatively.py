def print_alternate(arr):

    for i in range(0, len(arr)):
        for j in range(len(arr)-1-i, -1, -1):
            if len(arr)%2 == 0:
                if j != (len(arr) // 2):
                    print(arr[j], end=" ")
                    print(arr[i], end=" ")
                    break
                if j == (len(arr) // 2):
                    print(arr[j], end=" ")
                    print(arr[i], end=" ")
                    return ''
            else:
                if j != (len(arr) // 2)+1:
                    print(arr[j], end=" ")
                    print(arr[i], end=" ")
                    break
                if j == (len(arr) // 2)+1:
                    print(arr[j], end=" ")
                    print(arr[i], end=" ")
                    j -= 1
                    print(arr[j], end=" ")
                    return ''

#arr = [1,2,3,4,5,6,7]
arr = [1,2,3,4,5,6,7,8,9]
print(print_alternate(arr))
