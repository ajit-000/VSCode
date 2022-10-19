import math


def sumclosest(arr, x):
    arr.sort()
    closestSum = math.inf
    for i in range(len(arr)-2):
        ptr1 = i + 1
        ptr2 = len(arr) - 1
        while (ptr1 < ptr2):
            sum = arr[i] + arr[ptr1] + arr[ptr2]
            if sum==closestSum:
                return sum
            if (abs(x - sum) < abs(x - closestSum)):
                closestSum = sum
            if (sum > x):
                ptr2 -= 1
            else:
                ptr1 += 1
    return closestSum


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    x = int(input())
    print(sumclosest(lst, x))
