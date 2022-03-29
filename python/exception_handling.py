try:
    age=int(input("Enter your age: "))
    # print(x)
# except ValueError as e:
except NameError as e:
    print("The value you enter are not integer")
    print(e)
    print(type(e))
