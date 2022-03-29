#include <stdio.h>

int insert(int arr[], int index, int element, int n)
{
    for (int i = n - 1; i < index; i--)
    {
        arr[i + 1] = arr[i];
    }
    arr[index] = element;

    return 1;
}

int main()
{
    int arr[50], n, index, element;
    printf("Enter the Size of array you want : ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d element : ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("The elements of array are : \n");

    for (int j = 0; j < n; j++)
    {
        printf("%d ", arr[j]);
    }

    printf("\nEnter the index at which you want to insert element :\n");
    scanf("%d", &index);

    printf("Enter the element you want to insert :\n");
    scanf("%d", &element);

    insert(arr, index - 1, element, n);

    for (int k = 0; k < n; k++)
    {
        printf("%d ", arr[k]);
    }

    return 0;
}