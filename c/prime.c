#include <stdio.h>

int main()
{
    int low, high, i, flag;
    printf("Enter first number: ");
    scanf("%d", &low);
    printf("Enter second number: ");
    scanf("%d", &high);
    printf("Prime numbers between %d and %d are: ", low, high);

    while (low <=  high)
    {
        flag = 0;

        if (low <= 1)
        {
            ++low;
            continue;
        }

        for (i = 2; i <= low / 2; i++)
        {

            if (low % i == 0)
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        printf("%d ", low);

        ++low;
    }
    return 0;
}