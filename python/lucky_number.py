def number(num):
    for i in num:
        if '7' in i:
            print("Yes")
        else:
            print("No")


T = int(input("Enter the number of test cases "))
l = []
for i in range(T):
    A = input(f"Enter {i+1} number:")
    l.append(A)
number(l)
