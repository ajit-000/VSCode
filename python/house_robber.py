def rob(nums):
    ll = [[0, 0] for i in range(len(nums)+1)]
    for i in range(1, len(ll)):
        ll[i][0] = nums[i-1]+ll[i-1][1]
        ll[i][1] = max(ll[i-1][0], ll[i-1][1])
    print(ll)
    return max(ll[-1][0], ll[-1][1])



if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(rob(lst))
