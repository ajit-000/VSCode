N = int(input("Enter the length of String: "))
lst = []
for i in range(N):
    lst.append(input(f"Enter {i+1} value: "))
    if lst[i].isdigit():
        lst[i] = int(lst[i])
    else:
        continue
print(lst)

