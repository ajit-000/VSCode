def majelem(lst):
    cnt = 0
    major = lst[0]
    for i in lst:
        if cnt == 0:
            major = i
        if major == i:
            cnt += 1
        else:
            cnt -= 1
    return major


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(majelem(lst))
