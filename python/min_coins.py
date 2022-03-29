lst = [10, 20, 5]
k = 35
l1 = []
lst.sort(reverse=True)
for i in lst:
    if k >= i:
        l1.append(i)
        k -= i
print(l1)
