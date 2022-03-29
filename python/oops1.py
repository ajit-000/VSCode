# class Point:
#     defaut_colour = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point({self.x},{self.y})")


# point = Point.zero()
# point.draw()
# point.defaut_colour = "blue"
# print(point.defaut_colour)
# print(Point.defaut_colour)
# point.z = 30



# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def f(self):
#         x = 0
#         y = 10
#         print("T   ")

#     def s():
#         print("Y  ")


# ob = A(10, 20)
# print(ob.__dict__)





# class invalidEmployeeException(Exception):
#     pass


# class Project:
#     def __init__(self, employee_list):
#         self.__employee_list = employee_list

#     def validate_employee(self, employee_id):
#         flag = False
#         for key in self.__employee_list:
#             if(key == employee_id):
#                 flag = True
#         if flag == False:
#             raise invalidEmployeeException
#             print("1")
#         return True


# project1 = Project([1001, 1002, 1003])
# try:
#     print(project1.validate_employee(1005))
# except Exception:
#     print("2")
# except invalidEmployeeException:
#     print("3")
