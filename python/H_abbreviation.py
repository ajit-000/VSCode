def abbreviation(a, b):
    a = a.upper()
    if len(a)<len(b):
        return "NO"
    if len(b)==0:
        return "True"
    if a[0]==b[0]:
        return abbreviation(a[1:],b[1:])
    else:
        return abbreviation(a[1:],b)


if __name__ == "__main__":
    a = "beFgh"
    b = "EFH"
    print(abbreviation(a, b))
