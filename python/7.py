a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

# in python their is 'max' function defined in library which gives
# maximum of numbers provided
# syntax max(a,b,c)

print(max(a, b, c))

if a >= b:
    if a >= c:
        print(a, "is greater than", b, "and", c)

    else:
        print(c, "is greater then", a, "and", b)

else:
    if b >= c:
        print(b, "is greater then", a, "and", c)

    else:
        print(c, "is greater then", a, "and", b)
