# class A:
#     def test1(self):
#         print(" test of A called ")


# class B(A):
#     def test(self):
#         print(" test of B called ")


# class C(A):
#     def test(self):
#         print(" test of C called ")


# class D(B, C):
#     def test2(self):
#         print(" test of D called ")


# obj = D()
# obj.test()


# def fun(airline, source, destination, no_of_passengers):
#     ticket_number_list = []
#     for i in range(1, no_of_passengers+1):
#         ticket = airline+":"+source[0:3]+":"+destination[0:3]+":"+str(100+i)
#         ticket_number_list.append(ticket)
#     print(ticket_number_list)
#     if no_of_passengers < 5:
#         return ticket_number_list
#     else:
#         return ticket_number_list[no_of_passengers-5:no_of_passengers:1]


# print(fun("AI", "Bangalore", "London", 7))

# d={}
# print(all(d))
# print(any(d))

# class Person:

#     def __init__(self, person_name, person_age):
#         self.name = person_name
#         self.age = person_age

#     def __str__(self):
#         return f'Person name is {self.name} and age is {self.age}'

#     def __repr__(self):
#         return f'Person(name={self.name}, age={self.age})'


# p = Person('Pankaj', 34)

# print(p.__str__())
# print(p.__repr__)

# x=9
# y=list(range(0,3))
# print(repr(x))

# class Demo(object):
#     def __init__(self):
#         print('__init__() called...')

#     def __new__(cls, *args, **kwargs):
#         print('__new__() - {cls}'.format(cls=cls))
#         return object.__new__(cls, *args, **kwargs)


# if __name__ == '__main__':
#     de = Demo()


# tuple = {}
# tuple[(1,2,4)] = 8
# tuple[(4,2,1)] = 10
# tuple[(1,2)] = 12
# print(tuple)
# _sum = 0
# for k in tuple:
#     _sum += tuple[k]
# print(len(tuple) + _sum)
