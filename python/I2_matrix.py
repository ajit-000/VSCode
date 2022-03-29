# def printSubSeqRec(str, n, index=-1, curr=""):
#     # base case
#     lst = []
#     if (index == n):
#         return
#     if (len(curr) % 2 == 0 and curr[:len(curr)//2] == curr[len(curr)//2:]):
#         # print(len(curr))
#         lst.append(curr)

#     i = index + 1
#     while (i < n):
#         curr = curr + str[i]
#         printSubSeqRec(str, n, i, curr)
#         curr = curr[0:-1]
#         i = i + 1
#     # print(lst)
# # function


# def printSubSeq(str):
#     printSubSeqRec(str, len(str))


# # // Driver code
# str = input()
# t = str[::-1]
# x = printSubSeq(t)
# print(x)

def mat(s):
    reversedS = s[::-1]
    dp = [[0 for i in range(len(s) + 1)] for j in range(len(reversedS) + 1)]

    for i in range(len(s) - 1, -1, -1):
        for j in range(len(reversedS) - 1, -1, -1):
            if s[i] == reversedS[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    if dp[0][0]<=4:
        return dp[0][0]
    else:
        return dp[0][0]+1

s = input()
print(mat(s))
