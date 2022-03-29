class Ajit:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def sep_dash(cls, s):
        x = s.split("-")
        return cls(x[0], x[1])


aj = Ajit.sep_dash("AJIT-19")
print(aj.name)
print(aj.age)



# class Table:
#     def __init__(self):
#         self.no_of_legs = 4
#         self.glass_top = None
#         self.wooden_top = None

#     def identify_rate(self):
#         if(self.glass_top == True):
#             rate = 20000
#         elif(self.wooden_top == True):
#             rate = 30000
#         else:
#             rate = 0
#         return rate


# dining_table = Table()
# dining_table.glass_top=True
# print(dining_table.identify_rate())