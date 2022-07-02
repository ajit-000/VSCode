def checkpair(lst, k):
    rem = []
    for i in lst:
        rem.append(i % k)
    # print(rem)
    freq = [0]*k
    # print(freq)
    for i in rem:
        freq[i] += 1
    # print(freq)
    p, q = -1, k+1
    while p <= q:
        p += 1
        q -= 1
        if p == 0 or (k % p == 0 and p != 1):
            # print(p,q)
            if freq[p] % 2 == 0:
                continue
            else:
                return "Not all pairs are present"
        else:
            s = freq[p]+freq[k-p]
            # print(s)
            if s % 2 == 0:
                continue
            else:
                return "Not all pairs are present"

    return "All pairs are present"


if __name__ == "__main__":
    k = int(input("Enter the divisible term: "))
    n = int(input("Enter the length of your list: "))
    lst = [int(input()) for i in range(n)]
    print(checkpair(lst, k))
