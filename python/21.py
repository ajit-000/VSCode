n = int(input("Enter the number to count digits :"))
x = n
i = 0
while (n > 0):
    i = i+1
    n = n//10
print("Total number of digits in", x, "are :", i)
