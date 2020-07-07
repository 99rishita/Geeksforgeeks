def subarraysum(arr, k):
    sum = 0
    for i in range(0, len(arr)):
        sum = arr[i]
        #j = i+1
        for j in range(i+1, len(arr)):
            sum = sum + arr[j]
            if sum > k:
                break
            if sum == k:
                print(i+1)
                print(j+1)
                return

#arr = [1,2,3,7,5]
#k = 12
#arr = [1,2,3,4,5,6,7,8,9,10]
#k = 15
arr = [1, 4, 20, 3, 10, 5]
k = 33
subarraysum(arr, k)
            

