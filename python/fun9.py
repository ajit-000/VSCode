import math
import sys


def isprime(n1, n2):
    nums = []
    for i in range(n1, n2+1):
        x = int(math.sqrt(i))
        for j in range(2, x+1):
            if i % j == 0:
                break
        else:
            nums.append(i)
    return nums


print()
print("Prime numbers between a given range:")
print()
print("****PLEASE ENTER THE NUMBERS GREATER THAN 1****")
print()
n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))
print("The prime numbers between", n1, "and", n2, "are :", isprime(n1, n2))
