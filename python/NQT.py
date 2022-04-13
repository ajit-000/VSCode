def checkstr(s):
    s = list(s)
    lst = []
    count = 0
    x = len(s)
    if x > 100:
        return "Wrong Input"
    for i in range(x):
        if s[i].isalpha():
            lst.append(s[i])
        else:
            count += 1
    if x == count:
        return "Invalid String"
    s1 = map(str, lst)
    return "".join(s1)


s = input()
print(checkstr(s))
