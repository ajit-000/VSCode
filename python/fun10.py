def calci(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    return sum, sub, mul


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
sum, sub, mul = calci(a, b)
print("The addition of", a, "and", b, "is :", sum)
print("The substraction of", a, "and", b, "is :", sub)
print("The multiplication of", a, "and", b, "is :", mul)
