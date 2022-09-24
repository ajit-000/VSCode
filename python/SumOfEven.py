# def sumeven_brute(nums, queries):
#     res=[]
#     for i in queries:
#         cnt=0
#         nums[i[1]]+=i[0]
#         for j in nums:
#             if j%2==0:
#                 cnt+=j
#         res.append(cnt)
#     return res


def sumeven_opt(nums, queries):
    res = []
    even_sum = sum(i for i in nums if i % 2 == 0)
    for i in queries:
        if nums[i[1]] % 2 == 0:
            even_sum -= nums[i[1]]
        nums[i[1]] += i[0]
        if nums[i[1]] % 2 == 0:
            even_sum += nums[i[1]]
        res.append(even_sum)
    return res


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    n = len(nums)
    queries = []
    for i in range(n):
        elem = list(map(int, input().split()))
        queries.append(elem)
    print(sumeven_opt(nums, queries))
