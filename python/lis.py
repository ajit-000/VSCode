# import bisect


# def lis(arr):
#     dp = [arr.pop(0)]
#     for i in arr:
#         if i > dp[-1]:
#             dp.append(i)
#         else:
#             dp[bisect.bisect_left(dp, i)] = i
#     return dp


# if __name__ == "__main__":
#     nums = list(map(int, input().split()))
#     print(lis(nums))

def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] >= dp[i]:
                dp[i] = 1+dp[j]
    print(max(dp))


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    lis(arr)
