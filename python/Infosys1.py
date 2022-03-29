inarr = list(map(str, input().split(",")))
instr = input()
lst = []
x = 0
for i in inarr:
    l1 = list(instr[:])
    y = ''
    for j in range(len(i)):
        if i[j] in l1:
            y += str(i[j])
            l1.remove(str(i[j]))
        else:
            continue
    if y == i:
        lst.append(i)
    else:
        continue
print(lst)




# def checkString(s1, s2):

#     count = {s1[i]: 0 for i in range(len(s1))}

#     for i in range(len(s1)):
#         count[s1[i]] += 1

#     for i in range(len(s2)):
#         if (count.get(s2[i]) == None or count[s2[i]] == 0):
#             return False
#         count[s2[i]] -= 1
#     return True


# if __name__ == "__main__":
#     input_str = input().split(',')
#     test = input()
#     result = list()

#     for value in input_str:
#         if(checkString(test, value)):
#             result.append(value)
# if len(result) == 0:
#     print(-1)
# else:
#     print(','.join(result))
