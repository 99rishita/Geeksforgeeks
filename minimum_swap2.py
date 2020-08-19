# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    swap = 0
    temp = 0
    for j in range(0, n):
        while arr[j] != j+1:
            temp = arr[j]
            arr[j], arr[temp-1] = arr[temp-1], arr[j]
            swap += 1
    return swap