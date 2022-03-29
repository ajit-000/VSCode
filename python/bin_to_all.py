# USING INBUILT MODULE IN WHICH WE PAAS BASE
#  OF BINARY NUMBER i.e. 2 in print

def bin_to_all(num):
    a = int(num, 2)
    b = int(num, 8)
    c = int(num, 16)
    return a, b, c


num = input("Enter the number in binary to convert in decimal : ")
a, b, c = bin_to_all(num)
print("The binary, decimal, octal, hexa-decimal equivalant of",
      num, "is :", num, a, b, c)

# WITHOUT USING INBUILT METHOD

# def conv_to_dec(num):
#     dec = 0
#     p = len(num)-1
#     # p=1

#     for i in num:
#         dec += int(i)*(2**p)
#         p -= 1
#         # dec += int(i)*p
#         # p = p*2

#     return dec


# num = input("Enter the number to convert in decimal : ")
# print("The decimal Equivalant of", num, "is :", conv_to_dec(num))
