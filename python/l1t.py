# def list_fun(N, op):
#     id=input().split()
#     print(id)


# N = int(input("Enter the number of operation to perform:"))
# op = []
# for i in range(0, N):
#     x=input()
#     op.append(x)
# # print(op)
# list_fun(N, op)


# def print_even(test_list):
#     for i in test_list:
#         if i % 2 == 0:
#             yield i


# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print("The original list is : " + str(test_list))


# print("The even numbers in list are : ", end=" ")
# for j in print_even(test_list):
#     print(j, end=" ")


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = (i for i in l1 if i % 2 == 0)
# print(type(x))
# print(list(x))


# mylist = [1, 2, 3]
# myit = iter(mylist)
# # print(type(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit, "this is optional statement"))

# a={}
# a[2]=10
# a[1]=[2,4,6]
# print(a.get(2))

# arr = [1, 2, 3, 4, 5]
# x, y = 0, 0
# arr = sorted(arr)
# n = len(arr)
# for i in arr[0:n-1]:
#     x += i
# for j in arr[1:n]:
#     y += j

