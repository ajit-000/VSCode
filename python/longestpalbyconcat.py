from collections import Counter

words = ["cc","ll","gg"]
d=Counter(words)
res=0
for i in words:
    x="".join(reversed(i))
    if len(set(i))==1:
        p=len(i)
        if p%2==0:
            res+=p
        else:
            res+=p-1
        break
    if x in d:
        q=min(d[i],d[x])
        res+=4*q
        d[i]-=q
        d[x]-=q
print(res)
