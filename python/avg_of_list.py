def avg(l):
    # IF WE WILL TAKE A LIST FROM USER AND TRIES TO PASS
    # IT AND MAKE CHANGES TO IT
    # THEN WE GET AN ERROR

    # return sum(l)/len(l)

   # WITHOUT USING INBUILT MODULE "sum"
   
    total = len(l1)
    average = 0
    for i in l1:
        average += int(i)
    return average/total


num = int(input("Enter the length of list you want : "))
l1 = []
for i in range(num):
    insert = input(f"Enter {i+1} term : ")
    l1.append(insert)
print(l1)
print(f"The average of all elements of lists : {l1} is : {avg(l1)}")
