def number(a):
    for i in a:
        x,y,z=0,0,0
        a=i.split()
        for j in a:
            if j=='1':
                x+=1
            elif j=='2':
                y+=1
            else:
                z+=1
        if x>y and x>=z:
            print("INDIA")
        elif y>x and y>=z:
            print("ENG")
        else:
            print("Drawn")


N=int(input("Enter the number of test cases:"))
x=[]
for i in range(N):
    a=input(f"Enter the {i+1} series: ")
    x.append(a)
number(x)
    
