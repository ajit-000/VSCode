def superReducedString(s):
    res = []
    for i in s:
        if len(res) == 0 or res[-1] != i:
            res.append(i)
        else:
            res.pop()

    if len(res) != 0:
        return ''.join(res)
    return 'Empty String'


s = input()
superReducedString(s)
