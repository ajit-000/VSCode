# s1 = set(('abcdef'))
# print(s1)

# When any function is called it's return value will comes in
# place the positon where the function is called.

# When we forcefully gives the argument to the function it replace
# it's default value


# def multiplier(num, n):
#     return n*num


# n1 = int(input("Enter the number :"))
# n2 = int(input("How many times you want to multiply it :"))
# print(f"{n1} time {n2} is {multiplier(n1,n2)}")

# Here x is keyword argument so keyword arguments are always defined
# at the end in formal parameters else program will throws an error

# In call by value : The value which is passed to the function, if
# it is immutable then the value will paas 'BY VALUE' i.e the copy
# of the value is passed.

# def my_fun(x):
#     x = x*2
#     print(id(x))
#     print(x)


# x = 'hello'
# print(x)
# my_fun(x)
# print(id(x))

# Here list is mutable so python itself take it as
# 'BY REFRENCE' so address of both formal and actual parameter i.e.
# same list is pass to the function not it's copy.

# def fun1(str):
#     str.append(4)
#     print(id(str))
#     print(str)


# x = [1, 2, 3]
# print(x)
# fun1(x)
# print(id(x))
# print(x)

# Arbitary Argument:-

# def fun2(b, *a):
#     return b, a


# print(fun2(1, 2, 3, 4, 5, 6, 9, 0))


# kwargs :-

# IN kwargs if we  have to give another formal parameter then
# it is not allowed we only pass a parameter before dictionary(**).

# def fun3(**a):
#     print(type(a))
#     print(a)


# fun3(x=[1, 2, 3], y=(32, 43, 21), z={54, 25, 19},)
