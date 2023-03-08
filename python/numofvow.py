def solve(s):
    s = [i.lower() for i in s]
    n = len(s)
    a = 0
    b = n-1
    x = y = 0
    d = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    while a < b:
        if s[a] in d.keys():
            x += 1
        if s[b] in d.keys():
            y += 1
        a += 1
        b -= 1
    if x == y:
        return True
    return False


s = "textbook"
print(solve(s))
