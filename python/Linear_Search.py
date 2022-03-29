from itertools import permutations
s = list(map(str, input().split()))
l = sorted(permutations(s[0], int(s[1])))
for i in l:
    print("".join(i))
