# def swm_brute(arr, k):
#     n = len(arr)
#     res = []
#     for i in range(n-k+1):
#         maxm = arr[i]
#         for j in range(i,i+k):
#             maxm = max(maxm,arr[j])
#         res.append(maxm)
#     return res


def swm_med(arr,k):
    pass

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(swm_med(arr, k))

