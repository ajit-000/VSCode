# Brute-Force approach to solve Bus Station 10/24 test cases passes only


# def countDivisors(n) :
#     cnt = []
#     for i in range(1, (int)(math.sqrt(n)) + 1) :
#         if (n % i == 0) :
#             if (n / i == i) :
#                 cnt.append(i)
#             else :
#                 cnt.append(i)
#                 cnt.append(n//i)
#     return cnt

# def solve(a):
#     s=sum(a)
#     res=[]
#     lst=countDivisors(s)
#     # print(lst)
#     for i in range(len(lst)):
#         for j in range(len(a)):
#             if lst[i]<a[j]:
#                 break
#         else:
#             res.append(lst[i])
#     return sorted(res)


# Optimised Solution :


def Bus_Station(lst):
    sa = []
    res = []
    sa.append(lst[0])
    for i in range(1, len(lst)):
        sa.append(sa[i-1]+lst[i])
    for i in lst:
        if (lst[-1] % i == 0):
            continue
        j = 1
        while (lst[i]*j <= lst[-1]):
            if(lst[i]*j in sa):
                j += 1
            else:
                break
        else:
            res.append(lst[i])
    return res


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(Bus_Station(lst))
