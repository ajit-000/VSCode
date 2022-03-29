n = int(input("Enter the year :"))

if (n % 4 == 0) and (n % 100 != 0):
    print(n, "is leap year")

elif n % 400 == 0:
    print(n, "is leap year")

else:
    print(n,"is not a leap year")