def win_tic(lst, n):
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            cnt = 0
            s = lst[i]+lst[j]
            # print(s)
            for k in range(9):
                if str(k) in s:
                    cnt += 1
            # print(cnt)
            if cnt == 9:
                res += 1
    return res


if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(input())
    print(win_tic(lst, n))