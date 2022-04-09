# Solution in Complexity of O(n):

lst = list(map(int, input().split()))
st = []
res = []
l = len(lst)
for i in range(l-1, -1, -1):
    if len(st) == 0:
        res.append(-1)
        st.append(lst[i])
    else:
        while len(st) != 0:
            x = st.pop()
            if x > lst[i]:
                st.append(x)
                st.append(lst[i])
                res.append(x)
                break
        else:
            res.append(-1)
            st.append(lst[i])
res.reverse()
print(res)


# Solution in complexity of O(n^2):

# lst = list(map(int, input().split()))
# ll = len(lst)
# for i in range(ll):
#     for j in range(i+1, ll):
#         if lst[i] < lst[j]:
#             print(lst[j], end=" ")
#             break
#     else:
#         print("-1", end=" ")
