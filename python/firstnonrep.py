def check(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0)+1
    print(d)
    for i in s:
        if d[i] ==1:
            return i
    return -1 

if __name__ == "__main__":
    s = "abaacdbdf"
    print(check(s))
