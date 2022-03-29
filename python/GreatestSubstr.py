sequence=input() 
ss=input() 
dd={} 
f=0 
def dictionary12(ss,dict12): 
    for j in ss: 
        if j.lower() in dict12: 
            dict12[j.lower()]+=1 
        elif j.upper() in dict12: 
            dict12[j.upper()]+=1 
for i in sequence: 
    if i in dd: 
        print("New Language Error") 
        f=1 
        break 
    dd[i]=0 
if f==0: 
    l=[] 
    s=" " 
    for i in range(len(ss)-1): 
        if ss[i] ==" " and ss[i+1]==" ": 
            s+="" 
        elif ss[i]==" " and ss[i+1]!=" ": 
            s+=" " 
            l.append(s) 
            s=" " 
    l.append(" ") 
    res=" " 
    list12=ss.split() 
    a=0 
    for i in range(len(list12)): 
        st=" " 
        dictionary12(list12[i],dd) 
        for key,value in dd.items(): 
            for z in range(value): 
                st=st+key 
            dd[key]=0 
        res=res+st+l[i]     
    print(res,end=" ")