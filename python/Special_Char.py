s = "aa a234bc@ sad$ hsagd^"
s = s.replace(" ", "")
s = list(s)
res = []
cnt=0
# print(s)
for i in range(len(s)):
    if s[i].isalpha():
        continue
    if s[i].isdigit():
        continue
    else:
        res.append(s[i])
        cnt+=1
print(cnt)
print(res)
