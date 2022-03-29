def lcs(s1, s2):
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1[:n]


def solve(s):
    suffixes = []
    n = len(s)
    max_len = 0
    for i in range(n):
        suffixes.append(s[i:n])
    suffixes.sort()
    for a, b in zip(suffixes, suffixes[1:]):
        rtr = lcs(a, b)
        if len(rtr) > max_len:
            max_len = len(rtr)
    return max_len


s = input()
print(solve(s))
