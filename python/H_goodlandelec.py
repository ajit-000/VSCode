import sys

n,k=int(map(int,input().split()))
lst2 = list(map(int, input().split(",")))

for i in range(len(lst2)):
    if lst2[i]==0:
        for j in range(k):
            if lst2[i-j+k]==1:
                pass