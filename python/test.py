# l1 = [[1, 2], [3, 4]]
# zeros = [0]*5
# combined = zeros+l1
# print(combined)

# print((list(range(20))))
# print(list("hello world"))

# def printing(*var_len_arg):
#     print(var_len_arg, type(var_len_arg), sep=" ")


# printing(10, 20)
# printing(10)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# first, *rest, last = l1
# print(first, last, sep=" ")
# print(rest)

# l1 = ["a", 10, "b", 72, "c", 43]
# for i in enumerate(l1):
#     print(i)
# print(enumerate(l1))
# print(list(enumerate(l1)))

# n = int(input("Enter the number:"))
# if n%2 != 0:
#     print("Weird")
# else:
#     if n >= 5 and n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")

# s = input("Enter the string : ")
# for i in s:
#     if i == "," or i == ".":
#         print()
#     else:
#         print(i, end="")

# print([[x, y] for x in [0, 1, 2] for y in [3, 4, 5]])


# n = int(input("Enter the number:"))
# for x in [0,1,2]:
#     for y in [3,4,5]:
#         for z in [6,7,8]:
#             # print([x,y,z])
#             if x+y+z==n:
#                 print([x,y,z])
