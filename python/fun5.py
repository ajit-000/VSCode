def printsum(*elements):
    res = 0
    for i in elements:
        res = res+i
    return res

print(printsum(10,20,30))
print(printsum(50,40,30))