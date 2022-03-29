def subtract(x, y):

    while (y != 0):

        borrow = (~x) & y
        x = x ^ y

        y = borrow << 1

    return x


x = int(input("Enter the first value : "))
y = int(input("Enter the second value : "))
print(f"{x} - {y} is {subtract(x, y)}")
