# Fibonacci series


import sys
n = int(input("Number of terms in Fibonacci series you want  : "))
print("The", n, "terms of fibonacci series are : ")
if n < 1:
    print("Enter the number greater than 1")
    sys.exit()
elif n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    print(1, 1, end=" ")
    a = 1
    b = 1
    for i in range(3, n+1):
        c = a+b
        print(c, end=" ")
        a = b
        b = c


# BY RECURSION

# def series(n):
#     if n < 0:
#         print("Invalid Number")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return series(n-1)+series(n-2)


# n = int(input("Number of terms in Fibonacci series you want  : "))
# print(f"The {n} terms of fibonacci series are : {series(n-1)}")
