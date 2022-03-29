# print("This is basic calculator")
# print("Press 1 to ADD")
# print("Press 2 to SUBSTRACCT")
# print("Press 3 to MULTIPLY")
# n = int(input("Enter your choice :"))

# if n>0 and n<4:

#     a = int(input("Enter first number :"))
#     b = int(input("Enter second number :"))

#     if n == 1:
#         print("The addition of", a, "and", b, "is", a+b)

#     elif n == 2:
#         print("The substraction of", a, "and", b, "is", a-b)

#     else:
#          print("The multiplication of", a, "and", b, "is", a*b)

# else:
#     print("Enter the valid number from 1 to 3 only")

import sys
print("""This is basic calculator
Press 1 to ADD
Press 2 to SUBSTRACT
Press 3 to MULTIPLY""")
#Using ("""") in string we could wrire multi lines strings 
#and changing of lines also displays in output

n=int(input("Enter your choice :"))

if n not in (1,2,3) :
    print("Enter the valid number")
    sys.exit()

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if n == 1:     
    print("The addition of", a, "and", b, "is", a+b)

elif n == 2:
     print("The substraction of", a, "and", b, "is", a-b)

else:
     print("The multiplication of", a, "and", b, "is", a*b)