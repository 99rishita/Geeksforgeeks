# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    swaps = 0
    swaped = False
    #to find too chaotic condition
    for i in range(0, n):
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return
    #Bubble sort to calculate minimum number of bribes
    for i in range(0, n):
        for j in range(0, n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps += 1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    print(swaps)


