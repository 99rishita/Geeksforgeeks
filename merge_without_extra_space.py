def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    for i in range(m-1, -1, -1):
        last = arr1[n-1]
        j = n-2
        while(j >= 0 and arr1[j] > arr2[i]):
            arr1[j+1] = arr1[j]
            j -= 1
        if (j != n-2 or last > arr2[i]):
            arr1[j+1] = arr2[i]
            arr2[i] = last


arr1 = [1,5,9,10,15,20]
arr2 = [2,3,8,13]
merge(arr1, arr2)
print("After Merging \nFirst Array:", end="") 
for i in range(len(arr1)): 
    print(arr1[i] , " ", end="") 
  
print("\nSecond Array: ", end="") 
for i in range(len(arr2)): 
    print(arr2[i] , " ", end="") 
            

