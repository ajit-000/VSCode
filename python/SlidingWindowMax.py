# Naive Approach

lst = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
l = len(lst)
app = []
for i in range(l-k+1):
    res = lst[i:i+k]
    app.append(max(res))
print(app)
