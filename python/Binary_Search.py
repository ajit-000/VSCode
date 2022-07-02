# Iterative approach for Binary Search

def binary_search(lst, st, ed, elem):
    while st <= ed:
        mid = (st+ed)//2
        if lst[mid] == elem:
            return mid+1
        elif lst[mid] < elem:
            st = mid+1  # x in right side from mid
        else:
            ed = mid-1  # x in left side from mid
    return -1


print("\nEnter the elements of the list:")
lst = list(map(int, input().split()))
st = 0
ed = len(lst)-1
elem = int(input("Enter the number you want to find : "))
res = binary_search(lst, st, ed, elem)

if res == -1:
    print("Element is not present in the list")
else:
    print(elem, "is at", res, "position in the list")
