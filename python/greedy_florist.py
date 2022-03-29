def getMinimumCost(n, k, arr):
    s = 0
    arr.sort(reverse=True)
    if k == 0:
        return 0

    for i in range(n):
        s += (1+(i//k))*arr[i]
    return s


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(getMinimumCost(n, k, arr))
