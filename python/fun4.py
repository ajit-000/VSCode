def printelements(*se):
    print(se)


se = set()
size = int(input("Enter the size of tuple :"))

for i in range(size):
    x = input(f"Enter {i+1} element :")
    se.add(x)

y = printelements(se)
