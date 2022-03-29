def QuickSort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        QuickSort(lst, low, pi-1)
        QuickSort(lst, pi+1, high)
    return lst


def partition(lst, low, high):
    i = low-1
    pivot = lst[high]
    for j in range(low, high):
        i += 1
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1


print(QuickSort([34, 5, 67, 3, 12, 40, 9],
      0, len([34, 5, 67, 3, 12, 40, 9])-1))
