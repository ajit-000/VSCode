def alphainloop(char,nums):
    x=nums+ord(char)
    if (x)>90:
        return chr(65+(x)%90)
    return chr(x)

if __name__=="__main__":
    char="A"
    nums=10
    print(alphainloop(char,nums))