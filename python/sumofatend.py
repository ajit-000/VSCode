def sumse(lst):
    while len(lst)>2:
        n=len(lst)
        for i in range(n//2):
            lst[i]+=lst[n-1-i]
            lst.pop()
    return lst

if __name__=='__main__':
    lst=list(map(int,input().split()))
    print(sumse(lst))