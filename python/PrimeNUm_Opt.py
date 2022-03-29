# optimised program for prime numbers
import sys
import math
n = int(input("Enter the number to check prime : "))
if n <= 1:
    print("The number is not prime")
    sys.exit()
else:
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            print(n, "is not prime number")
            break
        i+=1
    else:
        print(n, "is prime number")
