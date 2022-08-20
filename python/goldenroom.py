def subArraySum(arr, n, sum_):
    currentSum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while currentSum > sum_ and start < i-1:
            currentSum = currentSum - arr[start]
            start += 1
        if currentSum == sum_:
            print(start+1, i)
            return 1
        if i < n:
            currentSum = currentSum + arr[i]
        i += 1
    print("-1")
    return 0


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    subArraySum(arr, n, k)
