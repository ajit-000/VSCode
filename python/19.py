n = int(input("Enter the number of row's in invert triangle : "))
for i in range(n+1):
    for j in range(n-i):
        print("*", end=" ")
    print()
