#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *x, n, y;

    printf("Enter the size of array you want :\n");
    scanf("%d", &n);

    x = (int *)malloc(n * sizeof(int));

    //inserting elements in array
    printf("\nEnter the elements in array :\n");
    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d element : ", i + 1);
        scanf("%d", &x[i]);
    }

    //sort array in upper order

    for (int j = 0; j < n; j++)
    {
        for (int k = j + 1; k < n; k++)
        {
            if (x[k] > x[j])
            {
                y = x[j];
                x[j] = x[k];
                x[k] = y;
            }
        }
    }

    printf("The sorted array is :\n");
    for (int l = 0; l < n; l++)
    {
        printf("%d\n", *(x + l));
    }

    // free(x);

    // printf("The elements of array are :\n");
    // for (int m = 0; m < n; m++)
    // {
    //     printf("%d\n", *(x + m));
    // }

    return 0;
}
