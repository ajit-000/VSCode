# x = input()
# m = 0
# for i in range(len(x)):
#     temp=""
#     for j in range(i, len(x)):
#         temp+=x[j]
#         m += int(temp)
# m=m%(10**9+7)
# print(m)


# Not Correct
def sam_str(lst):
    sum_ = 0
    x = [0]*len(lst)
    x[0] = int(lst[0])
    for i in range(1, len(lst)):
        x[i] = int(lst[i])*(i+1)+10*x[i-1]
        sum_ += x[i]
    return sum_ % (10**9+7)


if __name__ == "__main__":
    s = input()
    print(sam_str(s))
