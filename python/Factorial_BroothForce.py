# import sys
# n = int(input("Enter the number to find factorial :"))
# x = 1
# for i in range(2, n+1):
#     x = x*i
# print("The factorial of", n, "is :", x)

import math
n = int(input("Enter the number : "))
x = math.factorial(n)
print("The factorial of", n, "is :", x)
