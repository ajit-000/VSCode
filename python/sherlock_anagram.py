from collections import Counter

s = "abba"
s = list(s)
lst = []
m = {}
ag = 0
for i in range(len(s)):
    for j in range(len(s)-i):
        s1 = ''.join(sorted(s[j:j + i + 1]))
        m[s1] = m.get(s1, 0)+1
for k in m:
    ag += (m[k]-1)*m[k]//2
print(ag)
