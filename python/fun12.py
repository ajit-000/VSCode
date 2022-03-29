# import sys


# def firstdigit(num):
#     while num >= 9:
#         num = num//10
#     return num


# num = int(input("Enter the number :"))
# if num < 0:
#     print("Please enter the positive number")
#     sys.exit()
# else:
#     print("The first digit of", num, "is :", firstdigit(num))

import math
import sys


def lastdigit(num):
    x = int(math.log10(num))
    res = num//(10**x)
    return res


num = int(input("Enter the number :"))
if num < 0:
    print("Enter the positive value greater than 0")
    sys.exit()
else:
    print("The first digit of", num, "is:", lastdigit(num))
