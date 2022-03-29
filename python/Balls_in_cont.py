def organizingContainers(container):
    lst1, lst2 = [], []
    for i in range(len(container)):
        s, t = 0, 0
        for j in range(len(container)):
            s += container[i][j]
            t += container[j][i]
        lst1.append(s)
        lst2.append(t)
    # print(lst1, lst2)
    lst1.sort()
    lst2.sort()
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            continue
        else:
            return "Impossible"
    return "Possible"


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        print(organizingContainers(container))
