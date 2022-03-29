try:
    age = int(input("Enter age :"))
    fact = 10/age
except (NameError,ValueError,ZeroDivisionError):
    print("An Error...")
# except ValueError:
#     print("An Error...")
# except ZeroDivisionError:
#     print("Division by '0' not possible")
else:
    print("No Error Encountered")
