# all divisor of the number
#Not very efficient way to do work
#Examine code 27.py to have a look

# using for loop

# import sys
# n = int(input("Enter the number to find its all divisor : "))
# if n < 0:
#     print("Enter the positive number")
#     sys.exit()
# else:
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             print(i, end=" ")
# print(n, "are the divisors of", n)

# using while loop

import sys
n = int(input("Enter the number to find all the divisor : "))
if n < 1:
    print("Enter the valid number greater than 0")
    sys.exit()
else:
    i = 1
    while i < ((n//2)+1):
        if n % i == 0:
            print(i, end=" ")
        i = i+1
    print(n, "are the divisors of", n)
