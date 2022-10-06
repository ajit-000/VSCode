from collections import Counter


s="i am who i am"
lst=list(s.split())
d=Counter(lst)
res=[]
for i,j in d.items():
    if j>1:
        res.append(i)
print(" ".join(res))