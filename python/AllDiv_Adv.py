import math
n = int(input("Enter the number to find all it's divisor :"))
i = 1
while i*i < n:
    if n % i == 0:
        print(i, end=" ")
        print(n//i, end=" ")
    i += 1
if i*i == n:
    print(i)

# Using for loop
# If we use for loop then the numbers with perfect square
# are printed twice

# import math
# n = int(input("Enter the number to find all it's divisor :"))
# for i in range(1, int(math.sqrt(n))+1):
#     if n % i == 0:
#         print(i, end=" ")
#         print(int(n//i), end=" ")
