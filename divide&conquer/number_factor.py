def no_of_ways(n):
    #given the prob to find no. of ways of creating n with {1,3,4}
    if (n == 0) or (n==1) or (n==2):
        return 1
    if n==3:
        return 2
    subtract1 = no_of_ways(n-1)
    subtract2 = no_of_ways(n-3)
    subtract3 = no_of_ways(n-4)

    return subtract1+subtract2+subtract3

n = 5
print(no_of_ways(n))