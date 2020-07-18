def change_coin(n, c):
    res = 0
    m = len(c)
    j = m-1
    while j >= 0:
        while n >= c[j]:
            res = n-c[j]
            arr.append(c[j])
            n = res
        j -= 1

n = 2045
arr = []
c = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
change_coin(n,c)
print(arr)