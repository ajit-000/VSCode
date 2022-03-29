def eq_stack(s1, s2, s3):
    s1.reverse()
    s2.reverse()
    s3.reverse()
    for i in range(len(s1)-1):
        s1[i] += s1[i+1]
    for i in range(len(s2)-1):
        s2[i] += s2[i+1]
    for i in range(len(s3)-1):
        s3[i] += s3[i+1]
    s1.reverse()
    s2.reverse()
    s3.reverse()
    for j in min(s1, s2, s3):
        if j in s1 and j in s2 and j in s3:
            return j
    else:
        return -1


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
print(eq_stack(s1, s2, s3))
