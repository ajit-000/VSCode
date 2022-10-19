# def largestnum_brute(nums):

# .....Only 82 testcases passed....

#     res = ''
#     res+=str(nums[0])
#     n = len(nums)
#     for i in range(n-1):
#         n1, n2 = nums[i], nums[i+1]
#         comp1 = int(str(n1)+str(n2))
#         comp2 = int(str(n2)+str(n1))
#         if comp1 > comp2:
#             res += str(n2)
#         else:
#             res = str(n2)+res
#     return res


def largestnum_opt(lst):
    lst = [str(i) for i in lst]
    n = len(lst)
    if len(set(lst)) == 1 and lst[0] == '0':
        return '0'
    for i in range(n-1):
        for j in range(i+1, n):
            if int(str(i)+str(j)) < int(str(j)+str(i)):
                lst[i], lst[j] = lst[j], lst[i]
    return "".join(lst)


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(largestnum_opt(lst))
