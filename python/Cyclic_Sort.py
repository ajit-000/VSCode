def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def cyclesort(arr):
    i, n = 0, len(arr)
    while i < n:
        if i == arr[i]-1:
            i+=1
            continue
        else:
            swap(arr, i, arr[i]-1)
    return arr


if __name__ == "__main__":
    print("Insert element......cyclic sort: ")
    arr = list(map(int, input().split()))
    print(cyclesort(arr))
