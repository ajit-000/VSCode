import sys
n = int(input("Enter the number to check prime :"))
if n == 1:
    print("1 is neither prime nor composite")
    sys.exit()
else:
    for i in range(2, (n+1)//2):
        if n % i == 0:
            print(n, "is not prime number")
            break
    else:
        print(n, "is prime number")
