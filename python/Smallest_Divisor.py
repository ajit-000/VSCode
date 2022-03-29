# import sys
# n = int(input("Enter the number :"))
# if n < 2:
#     if n == 1:
#         print("Smallest divisor of 1 is : 1")

#     else:
#         print("Enter the positive integer greater than 0")
# print("The smallest divisors of", n, "is :")
# for i in range(2, n+1):
#     if n % i == 0:
#         print(i)
#         sys.exit()

import sys
n = int(input("Enter the number :"))
if n < 2:
    if n == 1:
        print("Smallest divisor of 1 is : 1")
        sys.exit()

    else:
        print("Enter the positive integer greater than 0")
        sys.exit()

print("The smallest divisors of", n, "is :")
i = 2
while i <= n:
    if n % i == 0:
        print(i)
        break
    i = i+1
