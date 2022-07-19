# Naive Approach : 

# def subsum_naive(lst):
#     n = len(lst)
#     cnt = []
#     res = []
#     for i in range(n-2):
#         res.append(lst[i:i+3])
#         cnt.append(sum(lst[i:i+3]))
#     return max(cnt)



def subsum_sw(lst):
    pass



if __name__ == "__main__":
    lst = list(map(int, input().split()))
    # print(subsum_naive(lst))
    print(subsum_sw(lst))
