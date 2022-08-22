def reshape(arr, p, q):
    lst = []
    elem = []
    m, n = len(arr), len(arr[0])
    if p*q != m*n:
        return arr
    for i in arr:
        for j in i:
            elem.append(j)
            if len(elem) == q:
                lst.append(elem)
                elem=[]
    return lst


if __name__ == "__main__":
    print("Enter the row and column of array you want to create: ")
    n, m = map(int, input().split())
    print("Enter the elements in array: ")
    arr = [[int(input()) for i in range(m)]for j in range(n)]
    print("Enter the new size of row and columns: ")
    p, q = map(int, input().split())
    print(reshape(arr, p, q))
