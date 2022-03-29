def tour(lst):
    count, p = 0, 0
    for i in range(len(lst)):
        x = lst[i][0]-lst[i][1]
        count += x
        if count < 0:
            p = i+1
            count = 0
    return p


if __name__ == "__main__":
    N = int(input())
    lst = []

    for i in range(N):
        a, b = map(int, input().split())
        lst.append([a, b])

    print(tour(lst))
