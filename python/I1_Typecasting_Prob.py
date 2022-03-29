from ast import Delete


def split_num_inbetween(N):
    inx5 = N.index(5)
    inx8 = N.index(8)
    z = map(str, N[inx5:inx8+1])
    num2 = int("".join(z))
    # print(num2)
    x = N[:inx5]
    y = N[inx8+1:]
    p = x+y
    num1 = sum(p)
    # print(num1)
    return num1+num2


N = list(map(int, input().split()))
print(split_num_inbetween(N))
