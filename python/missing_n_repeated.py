from typing import Counter


arr = list(map(int, input().split()))
lst = []
d = {}
# print(Counter(arr))
for i in arr:
    if i in d:
        lst.append(i)
        break
    else:
        d[i] = d.get(i, 0)+1
print(d)
for i in range(1, len(arr)+1):
    if i not in d:
        lst.append(i)
        break
print(lst)
