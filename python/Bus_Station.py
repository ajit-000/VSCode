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


def solve(a):
    sa = []
    d = {}
    res = []
    sa.append(a[0])
    d[a[0]] = 0
    for i in range(1, len(a)):
        sa.append(sa[i-1]+a[i])
        d[sa[i]] = i
    # print(sa)
    # print(d)
    m = sa[-1]
    for i in sa:
        if m % i != 0:
            continue
        else:
            j = 1
            while(i*j <= m):
                if(i*j in d):
                    j += 1
                else:
                    break
            else:
                res.append(i)

    return res


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    solve(lst)
    print(solve(lst))
