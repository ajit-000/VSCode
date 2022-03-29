def abs_perm(x, k):
    result = []
    for i in range(1, len(x)+1):
        for j in range(1, len(x)+1):
            if abs(x[j-1]-i) == k:
                result.append(x[j-1])
    return f"The desired list is : {result}"


if __name__ == "__main__":
    l = int(input("Enter the length you want : "))
    print("Enter the elements : ")
    elem = list(map(int, input().split()))
    diff = int(input("Enter the difference you want : "))
    print(abs_perm(elem, diff))
