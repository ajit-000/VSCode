#include <stdio.h>

int deletion(int arr[], int index, int n)
{
    for (int i = index; i < n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }
    return 1;
}

int main()
{
    int arr[20], n, index;

    printf("Enter the size of array : ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("Enter %d element: ", i + 1);
        scanf("%d", &arr[i]);
    }

    for (int k = 0; k < n; k++)
    {
        printf("%d ", arr[k]);
    }

    printf("\nEnter the index which you wants to delete : ");
    scanf("%d", &index);

    deletion(arr, index - 1, n);

    for (int j = 0; j < n - 1; j++)
    {
        printf("%d ", arr[j]);
    }

    return 0;
}