def keys(lst,n):
    s=[0]*n
    q=[0]
    s[0]=1
    res=0
    while len(q)>0:
        x=q.pop()
        for i in lst[x]:
            if s[i]==0:
                s[i]=1
                q.append(i)
    for i in s:
        if i==1:
            res+=1
    return (True if res==n else False)


if __name__=="__main__":
    n=int(input("Enter the length: "))
    lst=[]
    for i in range(n):
        x=list(map(int,input().split()))
        lst.append(x)
    print(keys(lst,n))