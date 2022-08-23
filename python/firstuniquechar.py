def check(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0)+1
    lst = []
    for i, j in d.items():
        if j == 1:
            lst.append(i)
    if len(lst)==0:
        return -1
    return lst


if __name__ == "__main__":
    s = "abaebc"
    print(check(s))
