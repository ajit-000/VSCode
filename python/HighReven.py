# n, m = list(map(int, input().split()))
# mat = [[int(input())for i in range(m)]for j in range(n)]
# # print(mat)
# stk = []
# res = []
# for i in range(len(mat)):
#     max1 = 0
#     for j in range(len(i)-1):
#         if stk[i][j] > max1:
#             max1 = stk[i][j]
#         stk.append(max1)
# print(stk)


# def uncommon_elem(s1, s2):
#     res = []
#     cmn = []
#     # print(s1,s2)
#     for i in range(len(s1)):
#         if s1[i] in s2:
#             cmn.append(s1[i])
#         else:
#             res.append(s1[i])
#     s2 = set(s2)
#     s2 = list(s2)
#     cmn = set(cmn)
#     cmn = list(cmn)
#     for j in cmn:
#         s2.remove(j)
#     return len(res)+len(s2)


# s1 = [1, 1, 2, 3, 4, 5, 5, 7, 6, 9, 10]
# s2 = [11, 12, 13, 4, 5, 6, 7, 18, 19, 20]
# # print(uncommon_elem(s1, s2))
# d = {}
# for i in range(len(s1)):
#     d[s1[i]] = d.get(s1[i], 0)+1
# print(d)
