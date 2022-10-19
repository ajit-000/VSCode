def contacts(queries):
    res = []
    d = {}
    for i, j in queries:
        if i == 'add':
            n = len(j)
            for k in range(n):
                w = ''
                for l in range(n-k):
                    w += j[l]
                d[w] = d.get(w, 0)+1
        else:
            if j in d:
                res.append(d[j])
            else:
                res.append(0)
    return res


if __name__ == "__main__":
    n = int(input())
    queries = []
    for i in range(n):
        x,y=input().split()
        queries.append([x,y])
    print(contacts(queries))
