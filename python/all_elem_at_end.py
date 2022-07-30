def find(arr, key):
    count = 0
    for i in arr:
        if i == key:
            arr.remove(i)
            arr.append(i)
    # for j in range(count):
    #     arr.remove(key)
    #     arr.append(key)
    return arr


if __name__ == "__main__":
    arr = [3, 1, 5, 3, 1, 3]
    key = 3
    print(find(arr, key))
