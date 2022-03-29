# program to find lcm of two numbers

# x = int(input("Enter first number : "))
# y = int(input("Enter second number : "))

# z = max(x, y)

# LCM using for loop

# for i in range(z, x*y+1):
#     if (i % x == 0) and (i % y == 0):
#         break
# print("The lcm of", x, "and", y, "is :", i)

# LCM using while loop

# while (z <= x*y):
#     if (z % x == 0) and (z % y == 0):
#         break
#     else:
#         z = z+1
# print("The lcm of", x, "and", y, "is :", z)

# using math module of python

import math

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

z = math.gcd(x, y)

print("The lcm of", x, "and", y, "is :", (x*y)//z)
