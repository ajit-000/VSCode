def isUgly(n):
    if n == 1:
        return True
    else:
        c = 2
        i = 0
        d = {}
        while(n > 1):
            if(n % c == 0):
                d[i] = c
                i += 1
                n = n / c
            else:
                c = c + 1
    for i in d.values():
        if i == 2 or i == 3 or i == 6:
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    print(isUgly(n))
