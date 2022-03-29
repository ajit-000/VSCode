def check_substr(s,l):
    for i in range(len(s)-l+1):
        ss=s[i:i+l]
        if len(ss)==len(set(ss)):
            print(ss)
        else:
            continue

if __name__=="__main__":
    s=input("Enter the string: ")
    l=int(input("Enter the length of substring you want : "))
    check_substr(s,l)


    # for i in range(0,len(string),k):
    #     s=string[i:i+k]
    #     p=set(s)
    #     for j in p:
    #         print(j,end="")
    #     print()