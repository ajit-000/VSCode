from collections import Counter

def intersect(nums1, nums2):
    lst=[]
    d1=Counter(nums1)
    d2=Counter(nums2)
    for i,j in d1.items():
        if i in d2:
            m=min(j,d2[i])
            while m>0:
                lst.append(i)
                m-=1
    return lst

if __name__=="__main__":
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    print(intersect(nums1,nums2))