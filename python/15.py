import sys
n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))
for i in range(n1, n2+1):
    if n1 < n2:
        for j in range(1, 11):
            print(i, "*", j, "=", i*j,end="  ")
    else:
        sys.exit()
    print("""
    """)
