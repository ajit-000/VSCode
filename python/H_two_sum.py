def twosum(a, target):
    for i in range(len(a)-1):
        x = target-a[i]
        if x in a[i+1:]:
            print([x, a[i]], end=" ")
        else:
            continue


a = [0, 2, 4, 3, 2, 1]
target = 4
twosum(a, target)
