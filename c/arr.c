#include <stdio.h>
int main()
{
    int arr[10] = {0,
                   1,
                   2,
                   3,
                   4,
                   5,
                   6,
                   7,
                   8,
                   9};
    int x = 5;
    if (arr[x] == arr[x + 1])
    {
        printf("%d", arr[x]);
    }
    else
    {
        printf("%d", arr[x + 1]);
    }
    return 0;
}
