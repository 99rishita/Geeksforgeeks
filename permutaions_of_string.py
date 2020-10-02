def permute(s, l, r):
    if l==r:
        print(''.join(s))
    for i in range(l, r+1):
        s[l], s[i] = s[i], s[l]
        permute(s, l+1, r)
        s[l], s[i] = s[i], s[l]

s = 'abc'
a = list(s)
l = 0
r = len(s)-1
permute(a,l,r)
