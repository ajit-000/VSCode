s = input()
s = list(s)
l = len(s)
cn=0
x = [(s[i], s[i+1]) for i in range(l-1)]
# print(x)
for i in range(len(x)):
    p = "".join(x[i])
    # print(p)
    if int(p) <= 26:
        cn += 1
if cn>0:
    q=len(x)-cn
    cn*=q
print(cn+1)
