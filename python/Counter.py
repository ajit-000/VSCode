from collections import Counter

ip = int(input())
shoe_sizes = Counter(map(int, input().split()))
sales_num = int(input())
income=0
for i in range(sales_num):
    sz,price=map(int,input().split())
    if shoe_sizes[sz]:
        income+=price
        shoe_sizes[sz]-=1
print(income)