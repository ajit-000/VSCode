lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
num1, num2 = [], []
n1 = lst[0]
n2 = lst[-1]
for i in lst:
    n1 = max(n1, i)
    num1.append(n1)
for i in range(len(lst)-1, -1, -1):
    n2 = max(n2, lst[i])
    num2.append(n2)
print(num1, num2)
