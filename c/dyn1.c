#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr;
    int n, i;

    printf("Enter the number of elements for the array :\n");
    scanf("%d", &n);

    // Dynamically allocate memory using malloc()
    ptr = (int *)malloc(n * sizeof(int));

    // Check if the memory has been successfully
    // allocated by malloc or not
    if (ptr == NULL)
    {
        printf("Memory not allocated.\n");
        exit(0);
    }
    else
    {
        // Memory has been successfully allocated
        printf("\nMemory successfully allocated using malloc.\n");

        printf("\nEnter the %d elements in array  :\n", n);

        // Get the elements of the array
        for (i = 0; i < n; ++i)
        {
            scanf("%d", &ptr[i]);
        }

        // Print the elements of the array
        printf("The elements of the array are: ");
        for (i = 0; i < n; ++i)
        {
            printf("%d, ", ptr[i]);
        }
    }
    return 0;
}