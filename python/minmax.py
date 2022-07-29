def minmax(lst):
    length=len(lst)
    for i in range(1,length):
        if lst[0]>lst[i]:
            temp=lst[0]
            lst[0]=lst[i]
            lst[i]=temp
    return(lst[0])

if __name__=="__main__":
    lst=list(map(int,input().split()))
    print(minmax(lst))
    
    #5 11 6 2 0 7