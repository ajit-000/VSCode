#include <stdio.h>

// int linearsearch(int arr[], int element, int size)
// {
//     for (int i = 0; i < size; i++)
//     {
//         if (arr[i] == element)
//         {
//             return i + 1;
//         }
//     }
//     return -1;
// }

int binarysearch(int arr[], int element, int size)
{
    int low, mid, high;
    low = 0;
    high = size - 1;
    if (arr[low] == element)
    {
        return low;
    }

    else if (arr[high] == element)
    {
        return high;
    }

    while (low <= high)
    {
        mid = (low + high) / 2;
        if (arr[mid] == element)
        {
            return mid + 1;
        }
        if (arr[mid] < element)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
}

int main()
{
    // Unsorted array for Linear search

    // int arr[] = {15, 43, 9, 13, 54, 63, 13, 75};

    // Sorted array for binary search

    int arr[] = {15, 43, 59, 130, 194, 263, 313, 475};

    int element, size;

    size = sizeof(arr) / sizeof(int);

    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\nEnter the element you want to search : ");
    scanf("%d", &element);

    // printf("The element %d is found at index %d", element,
    //        linearsearch(arr, element, size));

    printf("The element %d is found at index %d", element,
           binarysearch(arr, element, size));

    return 0;
}