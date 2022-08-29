from collections import Counter


def check(s):
    lst=[]
    d = Counter(s)
    for i, j in d.items():
        if j == 1:
            lst.append(i)
            break
    if len(lst) == 0:
        return -1
    for i in range(len(s)):
        if s[i]==lst[0]:
            return i+1


if __name__ == "__main__":
    s = input()
    print(check(s))
