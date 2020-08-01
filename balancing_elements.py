def balancing(arr):
    lefteven = []
    righteven = []
    leftodd = []
    rightodd = []
    even = 0
    odd = 0
    count = 0
    for i in range(0, len(arr)):
        lefteven.append(even)
        leftodd.append(odd)
        if i%2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
    lefteven.append(even)
    leftodd.append(odd)
    print("lefteven array is", end=" ")
    print(lefteven)
    print("leftodd array is", end=" ")
    print(leftodd)
    even = 0
    odd = 0
    for i in range(len(arr)-1, -1, -1):
        righteven.append(even)
        rightodd.append(odd)
        if i%2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
    righteven.append(even)
    rightodd.append(odd)
    print("righteven array is", end=" ")
    print(righteven)
    print("righttodd array is", end=" ")
    print(rightodd)
    for i in range(0, len(arr)+1):
        if (leftodd[i] + righteven[i]) == (lefteven[i] + rightodd[i]):
            count += 1
    print(count)

arr = [2,1,6,4]
#arr = [5,5,2,5,8]
balancing(arr)