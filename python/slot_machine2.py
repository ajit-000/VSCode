# A=["123","357","246"]
# ans=0
# for i in range(len(A[0])):
#     ans+=int(max(A,key=lambda x:x[i])[i])
# print(ans)

A=["123","530","246"]
A = [sorted(i) for i in A]

ans=0
for i in range(len(A[0])):
    max_ = A[0][i]
    for j in range(len(A)):
        if A[j][i] > max_:
            max_ = A[j][i]
    ans += int(max_)
print(max_)