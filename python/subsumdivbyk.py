
def solve(arr, k):
    d = {0: 1}  # Initialize sum as 0 base case
    s = 0
    res = 0
    for i in arr:
        s = (s+i) % k
        if s in d:
            res += d[s]
            d[s] += 1
        else:
            d[s] = 1
    print(res)
    

# def solve(arr,k):
#     n=len(arr)
#     mod=[0]*k
#     # print(mod)
#     cumSum=0
#     for i in range(n):
#         cumSum=cumSum+arr[i]
#         mod[((cumSum%k)+k)%k]+=1
#     # print(mod)
#     res=0
#     for i in range(1,k):
#         if mod[i]>1:
#             res+=(mod[i]*(mod[i]-1))//2
#     res+=mod[0]
#     print(res)

if __name__ == "__main__":
    solve([4, 5, 0, -2, -3, 1], 5)
    # arr=list(map(int,input().split()))
    # k=int(input("Enter number for divisibility: "))
    # print(solve(arr,k))
