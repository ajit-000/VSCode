# Naive Approach

# def strictly(nums):
#     n = len(nums)
#     for i in range(n):
#         tmp_nums = nums[0:i] + nums[i + 1: n]
#         for j in range(n - 2):
#             if tmp_nums[j] >= tmp_nums[j + 1]:
#                 break
#         else:
#             return True
#     return False


# Optimised Approach

def strictly(nums):
    stack = []
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            stack.append(i)

    if not stack:
        return True
    if len(stack) > 1:
        return False
    i = stack[0]
    return (i == 1 or nums[i-2] < nums[i]) or (i+1 == len(nums) or nums[i-1] < nums[i+1])


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(strictly(arr))
