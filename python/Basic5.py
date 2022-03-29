n = int(input("Enter the number :"))
if n > 0:
    if n % 2 == 0:
        print("The number is : Positive Even")
    else:
        print("The number is : Positive odd")

elif n < 0:
    if n % 2 == 0:
        print("The number is : Negative Even")
    else:
        print("The number is : Negative odd")

else:
    print("The number you entered is 0")
