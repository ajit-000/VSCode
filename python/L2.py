def ev_od(l1):
    even = []
    odd = []
    for i in l1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


l1 = []
size = int(input("Enter the size of list you want :"))
for i in range(size):
    val = int(input(f"Enter the {i+1} element : "))
    l1.append(val)
even, odd = ev_od(l1)
print(f"The even values of list are : {even}")
print(f"The odd values of list are : {odd}")
