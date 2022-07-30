# from collections import Counter


# def canpal(s):
#     _odd = 0
#     d = Counter(s)
#     for i in d.values():
#         if i % 2 == 0:
#             continue
#         _odd += 1
#     if _odd > 1:
#         return False
#     return True



# Using Logical Operators

def biman(s):
    b=0
    for i in s:
        b^=1<<ord(i)
    if b==0 or (b-1)&b==0:
        return True
    return False

if __name__ == "__main__":
    s = input("Enter the string: ")
    print(biman(s))

