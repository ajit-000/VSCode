from collections import Counter


# def majorityElement(nums):
#     d = Counter(nums)
#     n = len(nums)
#     for i, j in d.items():
#         if j > n//2:
#             return i
#     return False

def majelem(lst):
    cnt = 0
    major = lst[0]
    for i in lst:
        if cnt == 0:
            major = i
        if major == i:
            cnt += 1
        else:
            cnt -= 1
    return major


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(majorityElement(nums))
