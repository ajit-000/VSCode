def rev(st):
    string=st.split(" ")
    # print(string)
    lst=[]
    for i in string:
        lst.insert(0,i)
    # print(lst)
    return " ".join(lst)

if __name__=="__main__":
    st=input("Enter the string : ")
    print(rev(st))

# s = list(range(20))
# print(s)
