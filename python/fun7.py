def printdict(elements):
    for k, v in elements.items():
        print(f"{k} is {v}")


# printdict(id=1, name="ajit", marks=100)
# printdict(id=2, name="ahdj", marks=91)
dic = {}
size = int(input("""Enter the size of dictionary 
-> TREAT KEY AND VALUE AS 1 ELEMENT
"""))
for i in range(size):
    key = input(f"Enter the {i+1} key element :")
    value = input(f"Enter the {i+1} value element :")
    dic.update({key:value})
print(dic)
printdict(dic)