def nonrep(s):
    left, right = 0, 0
    length = len(s)
    se = set()
    mx = 0
    while right < length:
        while s[right] in se:
            se.remove(s[left])
            left += 1
        se.add(s[right])
        mx = max(mx, right-left+1)
        right += 1
    return max(mx, 0)


if __name__ == "__main__":
    arr = input()
    print(nonrep(arr))
