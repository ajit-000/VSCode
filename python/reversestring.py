# HERE WE ARE USING 'REVERSED' KEYWORD BY THIS WE WILL RETURN THE
# VALUE AS AN LIST,TUPLE OR SET

# str = input("Enter the string : ")
# print(list(reversed(str)))

# METHOD 2 VIA TAKING REV AS AN EMPTY STRING AND THEN
# MAKE REV= i + REV , so that new value of string is assinged
# previous to the value stored

# str = input("Enter the string : ")
# rev = ""
# for i in str:
#     rev = i+rev
# print(rev)

# WE WILL ALSO REVERSED IT VIA SLICING METHOD


str = input("Enter the string : ")
print(str[::-1])
