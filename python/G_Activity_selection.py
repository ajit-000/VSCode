s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
d = []
for i in range(len(s)):
    d.append([s[i], f[i]])
d.sort()
print(d[0][0], end=" ")
p = d[0][1]
d.remove(d[0])
for x, y in d:
    if p <= x:
        p = y
        print(x, end=" ")
    else:
        continue
