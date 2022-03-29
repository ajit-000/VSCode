def changefirst(s):
    for i in s.split(" "):
        s=s.replace(i,i.capitalize())
    return str(s)

s=input("Enter the string: ")
print(changefirst(s))