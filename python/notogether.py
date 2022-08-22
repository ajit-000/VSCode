def ways(n):
    first = 2
    second = 3
    res = 0
    for i in range(3, n + 1):
        res = first + second
        first = second
        second = res
    return res


n = int(input())
print("Total ways are: ", ways(n))
