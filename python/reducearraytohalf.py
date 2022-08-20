from collections import Counter


def redarr(arr):
    cnt = 0
    x = Counter(arr)
    hs = len(arr)//2
    freq = [i for i in x.values()]
    freq.sort(reverse=True)
    while hs > 0:
        hs -= freq[cnt]
        cnt += 1
    return cnt


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    # 7 3 3 3 3 2 2 5 5 5
    print(redarr(arr))
