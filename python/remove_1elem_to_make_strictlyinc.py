def strictly(nums):
    nums1 = nums[:]
    n = len(nums)
    cnt = 0
    for i in range(n):
        nums = nums[:i]+nums[i+1:]
        for j in range(n-2):
            if nums[j] > nums[j+1]:
                cnt=min(cnt,)
        nums = nums1
    return (True if cnt == 0 else False)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(strictly(arr))

#Incomplete