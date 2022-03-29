n, k = map(int, input().split())
lst = list(map(int, input().split()))
# pg_no = 0
# # prob = []
# res = 0
# for i in lst:
#     while i > 0:
#         pg_no += 1
#         prob=[x for x in range(1,k+1)]
#         i=i-k
#         k = abs(int(i)-k)
#         print(prob,":",pg_no)
#         # if pg_no in prob[:k]:
#         #     res += 1
# # print(res)

# 4 2 6 1 10

ans = 0
page = 1
for i in lst:
    for j in range(1, i+1):
        print(j, page)
        if j == page:
            ans += 1
        if j == i or j % k == 0:
            page += 1

print(ans)

