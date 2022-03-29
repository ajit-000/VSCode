def lownum(lst):
    num = int(input("Enter the number smaller than which we have to print : "))
    return [i for i in lst if int(i) <= num], num


def divisible_nums(lst):
    even = [i for i in lst if int(i) % 2 == 0]
    odd = [i for i in lst if int(i) % 2 != 0]
    return even, odd


n = int(input("Enter the length of list you want to create : "))
lst = []
for i in range(n):
    elem = input(f"Enter {i+1} term : ")
    lst.append(elem)

val, num = lownum(lst)
print("Elements lower then", num, "are :", val)
even, odd = divisible_nums(lst)
print("Even elements of list are :", even)
print("Odd elements of list are :", odd)
