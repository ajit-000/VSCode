# Optimised Solution in complexity O(n)

lst = list(map(int, input().split()))
l = len(lst)
st = []
res = []
for i in range(l):
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
print(res)



# Naive Solution complexity O(n^2):

# lst = list(map(int, input().split()))
# l = len(lst)
# for i in range(l-1, -1, -1):
#     for j in range(i, -1, -1):
#         if lst[j] > lst[i]:
#             print(lst[j], end=" ")
#             break
#     else:
#         print(-1, end=" ")
