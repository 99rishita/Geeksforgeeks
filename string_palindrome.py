from itertools import permutations

str1 = 'abc'

perm = [''.join(p) for p in permutations(str1)]

print(str(perm))

