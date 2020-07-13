def index_equi(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(0, len(arr)):
        total_sum -= arr[i]
        if total_sum == left_sum:
            print(i)
        left_sum += arr[i]

arr =[1,3,2,4]
index_equi(arr)