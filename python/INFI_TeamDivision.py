def solve(arr, last_index, S1, S2, lenS1, lenS2):

    if(last_index < 0):
        if(abs(lenS1 - lenS2) > 1):
            return 10**4
        return abs(S1 - S2)
    return min(solve(arr, last_index - 1, S1, S2, lenS1, lenS2),
               solve(arr, last_index - 1, S1 + arr[last_index], S2 - arr[last_index], lenS1 + 1, lenS2 - 1))


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    n = len(arr)
    total_sum = sum(arr)
    min_diff = solve(arr, n - 1, 0, total_sum, 0, n)
    print(int(total_sum/2 - min_diff/2), int(total_sum/2 + min_diff/2))
