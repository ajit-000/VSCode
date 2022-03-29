#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *x, n;

    printf("Enter the size of array you want :\n");
    scanf("%d", &n);

    x = (int *)calloc(n, sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d element of array :\n", i+1);
        scanf("%d", x+i);
    }

    for (int j = 0; j < n; j++)
    {
        printf("The value at %d location of array is : %d\n", j+1, x[j]);
    }

    // free(x);
    // //checking the value after free
    // for (int k = 0; k < n; k++)
    // {
    //     printf("%d\n", x[k]);
    // }

    printf("\nEnter the new size of array you want :\n");
    scanf("%d", &n);

    x = (int *)realloc(x, n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d element of array :\n", i+1);
        scanf("%d", &x[i]);
    }

    for (int j = 0; j < n; j++)
    {
        printf("The value at %d location of array is : %d\n", j+1, x[j]);
    }

    free(x);

    return 0;
}