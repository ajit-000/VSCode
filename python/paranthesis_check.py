# def isValid(s):
#     s=list(s)
#     l=len(s)
#     stk=[]
#     if s[0]==")" or s[0]=="]" or s[0]=="}":
#         return False
#     for i in range(l):
#         if s[i]=="(" or s[i]=="{" or s[i]=="[":
#             stk.append(s[i])
#         elif s[0]==")":
#             if len(s)==0 or stk.pop()!=")":
#                 return False
#         elif s[0]=="]":
#             if len(s)==0 or stk.pop()!="[":
#                 return False
#         elif s[0]=="}":
#             if len(s)==0 or stk.pop()!="{":
#                 return False
#     return len(stk)==0


# print(isValid(input()))

def paran_check(s):
    s = list(s)
    l = len(s)
    res = []
    if s[0] == ")" or s[0] == "]" or s[0] == "}":
        return False
    else:
        d = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in d.keys():
                res.append(i)
            else:
                if res == []:
                    return False
                a = res.pop()
                if i != d[a]:
                    return False
        return res == []


s = input("Enter Parenthesis: ")
print(paran_check(s))
