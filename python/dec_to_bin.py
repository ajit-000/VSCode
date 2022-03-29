# BY INBUILT METHOD "bin()"
# IT WILL RETURN THE VALUE AS 0b-binary value
# SO WE HAVE TO PRINT AFTER 2 DIGITS TO GET PROPER RESULT

# num = int(input("Enter the number to convert in binary : "))
# x = bin(num)
# print(x[2:])

# WITHOUT USING INBUILT MODULE


import sys


def conv_to_bin(num):
    if num == 0:
        return 0
        sys.exit()
    else:
        binary = ""
        while num > 0:
            binary = binary + str(num % 2)
            num = num//2

        return binary[::-1]


num = int(input("Enter the number to convert in binary : "))
print("The binary form of", num, "is :", conv_to_bin(num))
