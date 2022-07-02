def checkPal(S):
    sublst = []
    res = 0
    for i in range(len(S)):
        substr = ""
        for j in range(0, i+1):
            substr += S[j]
        sublst.append(substr)
    # print(sublst)
    for i in sublst:
        if len(i) == 1:
            res += 1
            continue
        else:
            lst = list(i)
            cnt = 0
            s = set(i)
            # print(s)
            for j in s:
                x = lst.count(j)
                if x % 2 != 0:
                    cnt += 1
                else:
                    continue
                if cnt > 1:
                    break
            if cnt <= 1:
                res += 1
    return res


s = input("Enter the string: ")
print(checkPal(s))
# checkPal(s)
