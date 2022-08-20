def betmax(arr, n, k):
    res,temp,j,i=0,0,0,0
    while j<n:
        temp+=arr[j]
        if temp<k:
            j+=1
        else:
            temp-=arr[i]
            i+=1
            j+=1
        res=max(res,j-i)
    return res
    


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(betmax(arr, n, k))
