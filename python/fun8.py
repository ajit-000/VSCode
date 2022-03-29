def printdetails(id, **dic):
    # for i in id:
    print(f"The details of {id} is :")
    for k, v in dic.items():
        print(f"{k} is {v}")


printdetails(101, name="Ajit", marks=100)
print()
printdetails(102, name="ABH", marks=110, feature="chattu")
# d = {}
# l = list()
# size = int(input("Enter the size of dictionary : "))
# for i in range(size):
#     l.append(i+1)
# print(l)
# for j in range(size):
#     k = input(f"Enter {j+1} Name :")
#     v = input(f"Enter {j+1} Marks :")
#     d.update({k: v})
# print(d)
# printdetails(l, d)
