def maxSubarray(arr):
    s1 = 0
    lst = []
    l = len(arr)
    for i in range(l):
        if arr[i] > 0:
            s1 += arr[i]
    if s1 <= 0:
        s1 = max(arr)
    for i in range(l-1, -1, -1):
        for j in range(i, -1, -1):
            s2 = 0
            s2 += sum(arr[j:i+1])
            # print(s2)
            lst.append(s2)
    su = max(lst)
    return [su, s1]


print(maxSubarray([-2, -3, -1, -4, -6]))
