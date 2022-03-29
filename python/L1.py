def list_elem(l1, x):
    res = []
    for i in l1:
        if i <= x:
            res.append(i)
    return res


l1 = [10, 23, 51, 67, 9, 3, 1, 25]
l1.sort()
print(l1)
x = int(input("Enter the largest number below which you have to discard :"))
p = list_elem(l1, x)
print("The list you want is :", p)
