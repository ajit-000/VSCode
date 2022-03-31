num = int(input())
lst = input()
n, t = 0, 0
for i in lst:
    if i == "N":
        n += 1
    else:
        t += 1
if n > t:
    print("Nutan")
else:
    print("Tusla")
