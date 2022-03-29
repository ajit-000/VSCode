import sys


def firstdigit(num):
    x = num % 10
    return x


num = int(input("Enter the number :"))
if num < 0:
    print("Please enter the positive number")
    sys.exit()
else:
    print("The last digit of", num, "is :", firstdigit(num))
