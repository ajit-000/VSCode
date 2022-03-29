def items(l):

    # THIS METHOD IS NOT VERY EFFICIENT
    # BEST WAY TO COUNT DISTINCT ITEMS ARE BY USING "SET"
    # SINCE ALL THE ELEMENTS IN SET ARE DISTINCT

    # res = 1
    # for i in range(1, len(l)):
    #     if l[i] not in l[0:i]:
    #         res += 1
    # return res

    # WE CONVERT LIST INTO SET
    # AND RETURNING THE LENGTH OF SET

    return (len(set(l)))


n = int(input("Enter the size of list you want : "))
l1 = []
for i in range(n):
    num = input(f"Enter {i+1} item : ")
    l1.append(num)
print(f"Their are {items(l1)} distinct items present in the list")
