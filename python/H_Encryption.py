import math

"""
myna
meis
ajit
"""


def encryption(s):
    p = ""
    sm = s.replace(" ", "")
    a1 = math.floor(math.sqrt(len(sm)))
    a2 = math.ceil(math.sqrt(len(sm)))
    for i in range(0, a2):
        temp = []
        j = 0
        while(i+j < len(sm)):
            temp.append(sm[i+j])
            j += a2
        print(p.join(temp), end=" ")


s = input()
encryption(s)
# print(encryption(s))
