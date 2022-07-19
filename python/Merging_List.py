def mergeTwoLists(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    i, j = 0, 0
    res = []
    while i < l1 and j < l2:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    while j < l2:
        res.append(list2[j])
        j += 1
    
    while i < l1:
        res.append(list1[i])
        i += 1
    return res


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [1, 3, 4]
    print(mergeTwoLists(list1, list2))
