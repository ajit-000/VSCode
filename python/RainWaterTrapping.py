# Brute Force

# def trap_brute(height):
#     res = 0
#     n = len(height)
#     for i in range(n):
#         left = right = height[i]
#         for j in range(i):
#             left = max(left, height[j])
#         for k in range(i+1, n):
#             right = max(right, height[k])
#         res += (min(left, right)-height[i])
#     return res


# Better Solution

# def trap_better(height):
#     res = 0
#     length = len(height)
#     left, right = [], [0]*length
#     pref_sum = height[0]
#     suf_sum = height[-1]
#     for i in height:
#         pref_sum = max(pref_sum, i)
#         left.append(pref_sum)
#     for j in range(length-1, -1, -1):
#         suf_sum = max(suf_sum, height[j])
#         right[j]=suf_sum
#     #print(left,right)
#     for k in range(length):
#         res = res + min(left[k], right[k])-height[k]
#     return res


# Optimised Solution

def trap_opt(height):
    n = len(height)
    left = 0
    right = n-1
    l_max, r_max = 0, 0
    trap = 0
    while left <= right:
        if l_max <= r_max:
            trap += max(0, l_max-height[left])
            l_max = max(l_max, height[left])
            left += 1
        else:
            trap += max(0, r_max-height[right])
            r_max = max(r_max, height[right])
            right -= 1
    return trap


if __name__ == "__main__":
    height = list(map(int, input().split()))
    print(trap_opt(height))
