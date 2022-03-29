# s = ["abc", "dab", "bc"]
# x = []
# y = []
# for i in range(len(s)+1):
#     for j in range(i):
#         x.append(s[j:i])
# pp = list(sorted(x, key=len))
# print(pp)
# # for i in range(pp):
# #     print(pp[i], ":", i)

from itertools import combinations


def power(iterable):
    x = []
    for j in range(1, len(iterable)+1):
        for i in combinations(iterable, j):
            x.append(i)
    return x


n = int(input())
s = input().split(",")
ch = input().split(",")
# print(list(power(s)))

ob = list(power(s))

for i, j in enumerate(ob):
    if list(j) == ch:
        print(i+2)
        break
