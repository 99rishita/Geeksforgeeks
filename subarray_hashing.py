def hash_subarray(arr, k):
    map = {}
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
        if sum == k:
            print("sum found between indexes 1 to", i+1)
            return
        if (sum - k) in map:
            print("sum is found between indexes", map[sum-k]+2, "to", i+1)
            return

        map[sum] = i
    print("No subarray with given sum exists")

arr = [1,2,3,7,5]
k = 12
#arr = [10, 2, -2, -20, 10] 
#k = -10
#arr = [-10, 0, 2, -2, -20, 10]
#k = 20
#ar = [1, 4, 20, 3, 10, 5]
#ki = 33
hash_subarray(arr, k)