def largestrec(arr):
    n = len(arr)
    lst=arr[:]
    max_sum=0
    for i in range(n):
        max_len=0
        arr=lst[:]
        elem = lst[i]
        cnt = 0
        for j in range(n):
            arr[j] = arr[j]-elem
        for k in arr:
            if k>=0:
                cnt+=1
                max_len=max(max_len,cnt)
            else:
                cnt=0
        print(arr,max_len,elem)
        curr_sum = elem * max_len
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(largestrec(arr))
