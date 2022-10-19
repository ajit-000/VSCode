from collections import Counter

s="i am who i am"
find='i'
lst=list(s.split())
d=Counter(lst)
if find in d:
    print(d[find])
else:
    print(-1)