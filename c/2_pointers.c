#include <stdio.h>

int main()
{
    int a[20], b[20], len;
    printf("Enter the length of both arrays you want :\t");
    scanf("%d", &len);
    printf("Enter the elements of first array:\n");
    for (int i = 0; i < len; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("Enter the elements of second array:\n");
    for (int i = 0; i < len; i++)
    {
        scanf("%d", &b[i]);
    }
    printf("\n");
    for (int j = 0; j < len; j++)
    {
        printf("(%d,%d)\t(%d,%d)\n", a[j], b[len - 1 - j], a[j], b[j]);
    }
}