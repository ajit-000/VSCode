def twoSum(nums, target):
        d={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in d:
                return [i,d[diff]]
            d[j]=i

lst=list(map(int,input().split()))
target=int(input())
print(twoSum(lst,target))