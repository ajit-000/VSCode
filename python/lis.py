def lis(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        res=0
        for j in range(i):
            if arr[i]>arr[j]:
                if dp[j]>res:
                    res=dp[j]
        dp[i]=res+1
    print(dp)

if __name__=="__main__":
    arr=list(map(int,input().split()))
    lis(arr)
    