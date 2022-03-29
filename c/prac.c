#include <stdio.h>
#include <stdlib.h>

void printarray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("The value at %d index is: %d\n", i + 1, A[i]);
    }
}



int main()
{
    int n;
    printf("Enter the size of array you want : ");
    scanf("%d", &n);
    int *A = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d number: ", i + 1);
        scanf("%d", &A[i]);
    }
    printarray(A, n);
    return 0;
}