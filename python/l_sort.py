def sort_list(l):
    l1 = sorted(l)
    if l1 == l:
        return True
    return False


n = int(input("Enter the size of list you want : "))
l1 = []
for i in range(n):
    num = input(f"Enter {i+1} item : ")
    l1.append(num)
x = int(sort_list(l1))
if x == 1:
    print("The list is sorted")
else:
    print("List is not sorted")
