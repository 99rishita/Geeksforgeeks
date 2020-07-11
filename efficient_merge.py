def find_gap(gap):
    if gap<=1:
        return 0
    return (gap // 2) + (gap%2)

def merge_efficient(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = m+n
    find_gap(gap)
    while gap > 0:

        #comparing the elements in first array
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            i += 1

        #comparing elements of both the arrays
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        #comparing elements in second array
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                j += 1
        gap = find_gap(gap)


arr1 = [1,5,9,10,15,20]
arr2 = [2,3,8,13]
merge_efficient(arr1, arr2)
print("After Merging \nFirst Array:", end="") 
for i in range(len(arr1)): 
    print(arr1[i] , " ", end="") 
  
print("\nSecond Array: ", end="") 
for i in range(len(arr2)): 
    print(arr2[i] , " ", end="") 
