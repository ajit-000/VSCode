# Optimised Solution in O(n):


def nextGreaterElementToRight(arr, n):
    s = []
    v = []
    for i in range(n-1, -1, -1):
        while(len(s) != 0 and s[-1] <= arr[i]):
            s.pop()
        if len(s) == 0:
            v.append(-1)
        else:
            v.append(s[-1])
        s.append(arr[i])
    v.reverse()
    return v


if __name__ == '__main__':

    arr = list(map(int, input().split()))
    ans = nextGreaterElementToRight(arr, len(arr))
    print(ans)




# Solution in complexity of O(n^2):

# lst = list(map(int, input().split()))
# ll = len(lst)
# for i in range(ll):
#     for j in range(i+1, ll):
#         if lst[i] > lst[j]:
#             print(lst[j], end=" ")
#             break
#     else:
#         print("-1", end=" ")
