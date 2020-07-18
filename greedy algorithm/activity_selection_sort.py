def activity_selection(activity, s, f):
    n = len(activity)
    res = sorted(f)
    j = 0
    count = 0
    prev_activity = activity[j]
    print(activity[j], end=" ")
    count += 1
    #compare finish time of previous activity with start time of current activity
    for i in range(1, n):
        if f[j] <= s[i]:
            print(activity[i], end=" ")
            j = i
            count += 1
    print('\nNo. of activities selected are:')
    print(count)

activity = ['a1','a2','a3','a4','a5','a6']
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
activity_selection(activity, s , f)