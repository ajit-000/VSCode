#Heap Approach for E.T.L

from heapq import heapify,heappop,heappush
sz, sw = map(int, input().split())
lst = list(map(int, input().split()))
x=0
heapify(lst)
try:
    while min(lst)<sw:
        x+=1
        x1=heappop(lst)
        x2=heappop(lst)
        heappush(lst,x1+(2*x2))
        print(x)
except:
    print("-1")



# Stack Approach

# sz, sw = map(int, input().split())
# lst = list(map(int, input().split()))
# x=0
# while min(lst)<=sw:
#     x+=1
#     x1 = min(lst)
#     lst.remove(x1)
#     x2 = min(lst)
#     lst.remove(x2)
#     lst.insert(0, x1+(2*x2))
# print(x)
