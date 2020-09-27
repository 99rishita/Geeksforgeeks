b = 'vmmmoooonnjkkeeeyyyr'
a = list(b)
i = 0
while i < len(a)-1:
    if a[i]==a[i+1]:
        a.pop(i)
    else:
        i+=1
print(''.join(a))
