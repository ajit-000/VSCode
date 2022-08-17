def printSubsequences(arr, index, subarr):
    if index == len(arr):
        # Condition to avoid printing
        # empty subsequence
        if len(subarr) != 0:
            print(subarr)
    else:
        # Subsequence without including
        # the element at current index
        printSubsequences(arr, index + 1, subarr)
        # Subsequence including the element
        # at current index
        printSubsequences(arr, index + 1, subarr+[arr[index]])
    return


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    printSubsequences(arr, 0, [])
