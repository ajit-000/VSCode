def add_rev_pal(n):
    sn = str(n)
    while n != int(sn[::-1]):
        n += int(sn[::-1])
        sn = str(n)
    return f"{n} is pallindom now"



def check_pal(n):
    sn = str(n)
    if sn == sn[::-1]:
        return f"{n} is pallindrom"
    else:
        return add_rev_pal(n)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(check_pal(n))
