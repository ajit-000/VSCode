def binary_search_rec(lst, st, ed, elem):
    if ed >= st:
        mid = (st+ed)//2
        if lst[mid] == elem:
            return mid
        elif lst[mid] > elem:
            return binary_search_rec(lst, st, mid-1, elem)
        else:
            return binary_search_rec(lst, mid+1, ed, elem)
    else:
        return -1


print("\nEnter the elements of the list:")
lst = list(map(int, input().split()))
st = 0
ed = len(lst)-1
elem = int(input("Enter the number you want to find : "))
res = binary_search_rec(lst, st, ed, elem)

if res == -1:
    print("Element is not present in the list")
else:
    print(elem, "is at", res+1, "position in the list")
