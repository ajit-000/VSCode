# def swappair_brute(arr1, arr2):
#     sum_1, sum_2 = sum(arr1), sum(arr2)
#     for i in arr1:
#         for j in arr2:
#             newsum1 = sum_1-i+j
#             newsum2 = sum_2+i-j
#             if newsum1 == newsum2:
#                 return [i, j]
#     return -1

def swappair_opt(arr1, arr2):
    pass


if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(swappair_opt(arr1, arr2))

