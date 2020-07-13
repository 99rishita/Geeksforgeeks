def equi_point(arr):
    n = len(arr)
    left_sum = 0
    right_sum = 0
    i=0
    if n%2 == 1:
        while(i!=(n//2)):
            left_sum += arr[i]
            i += 1
        i += 1
        while(i!=n):
            right_sum += arr[i]
            i += 1
        if left_sum == right_sum:
            print(n//2)
    if n%2 == 0:
        while(i!=(n//2)):
            left_sum += arr[i]
            i += 1
        print(left_sum)
        i += 1
        while(i!=n):
            right_sum += arr[i]
            i += 1
        if left_sum == right_sum:
            print(n//2)

#arr = [1,4,6,2,3]
#arr = [-7,1,5,2,-4,3,0]
#arr = [1,3,2,4]
arr = [2,3,4,1,4,5]
equi_point(arr)