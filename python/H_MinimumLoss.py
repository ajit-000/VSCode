def minimumLoss(price):
    d = {}
    n = len(price)
    for i in range(n):
        d[price[i]] = i
    price.sort(reverse=True)
    res = price[0]
    for i in range(n-1):
        if d[price[i]] < d[price[i+1]]:
            res = min(res, price[i]-price[i+1])
    return res


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(minimumLoss(lst))
