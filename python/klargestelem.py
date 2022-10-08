import heapq as hq


def FirstKelements(arr, size, k):
    minHeap = []

    for i in range(k):
        minHeap.append(arr[i])
    hq.heapify(minHeap)

    for i in range(k, size):
        if minHeap[0] > arr[i]:
            continue
        else:
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            minHeap.append(arr[i])
            hq.heapify(minHeap)
    for i in minHeap:
        print(i, end=" ")


arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(arr)
k = 3
FirstKelements(arr, size, k)

# lst=[1,17,8,5,12,0,9]
# print(lst)
# heapq.heapify(lst)
# print(lst)
# heapq._heapify_max(lst)
# print(lst)
