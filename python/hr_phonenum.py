def getPhoneNumber(s):
    lst = []
    s = list(s.split(" "))
    l = len(s)
    for i in range(l):
        if s[i] == "double":
            if s[i+1] == "one":
                lst.append("1")
                # lst.append("1")
            elif s[i+1] == "two":
                lst.append("2")
                # lst.append("2")
            elif s[i+1] == "three":
                lst.append("3")
                # lst.append("3")
            elif s[i+1] == "four":
                lst.append("4")
                # lst.append("4")
            elif s[i+1] == "five":
                lst.append("5")
                # lst.append("5")
            elif s[i+1] == "six":
                lst.append("6")
                # lst.append("6")
            elif s[i+1] == "seven":
                lst.append("7")
                # lst.append("7")
            elif s[i+1] == "eight":
                lst.append("8")
                # lst.append("8")
            elif s[i+1] == "nine":
                lst.append("9")
                # lst.append("9")
            elif s[i+1] == "zero":
                lst.append("0")
                # lst.append("0")
        elif s[i] == "triple":
            if s[i+1] == "one":
                lst.append("1")
                lst.append("1")
                # lst.append("1")
            elif s[i+1] == "two":
                lst.append("2")
                lst.append("2")
                # lst.append("2")
            elif s[i+1] == "three":
                lst.append("3")
                lst.append("3")
                # lst.append("3")
            elif s[i+1] == "four":
                lst.append("4")
                lst.append("4")
                # lst.append("4")
            elif s[i+1] == "five":
                lst.append("5")
                lst.append("5")
                # lst.append("5")
            elif s[i+1] == "six":
                lst.append("6")
                lst.append("6")
                # lst.append("6")
            elif s[i+1] == "seven":
                lst.append("7")
                lst.append("7")
                # lst.append("7")
            elif s[i+1] == "eight":
                lst.append("8")
                lst.append("8")
                # lst.append("8")
            elif s[i+1] == "nine":
                lst.append("9")
                lst.append("9")
                # lst.append("9")
            elif s[i+1] == "zero":
                lst.append("0")
                lst.append("0")
                # lst.append("0")
        else:
            if s[i] == "one":
                lst.append("1")
            elif s[i] == "two":
                lst.append("2")
            elif s[i] == "three":
                lst.append("3")
            elif s[i] == "four":
                lst.append("4")
            elif s[i] == "five":
                lst.append("5")
            elif s[i] == "six":
                lst.append("6")
            elif s[i] == "seven":
                lst.append("7")
            elif s[i] == "eight":
                lst.append("8")
            elif s[i] == "nine":
                lst.append("9")
            elif s[i] == "zero":
                lst.append("0")
    return "".join(lst)


s = "five one zero two four eight zero double three two"
print(getPhoneNumber(s))