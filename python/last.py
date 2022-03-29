# Program to find last digit of number

# First we take input as positive number

# n = int(input("Enter the number :"))
# # take last digit as ld
# ld = n % 10
# print("The last digit of", n, "is :", ld)


# Take input as negative number
# Here we use 'abs' to take absolute value

n = int(input("Enter the number :"))
# take last digit as ld
ld = abs(n) % 10
print("The last digit of", n, "is :", ld)
