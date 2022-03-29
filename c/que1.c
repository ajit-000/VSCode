#include <stdio.h>
int main()
{
    int number, reverseofnumber, result, a, b;
    printf("Enter the 2-digit number :");
    scanf("%d", &number);
    a = number / 10;
    b = number % 10;
    reverseofnumber = b * 10 + a;
    printf("The reverse of %d is %d\n", number, reverseofnumber);
    if (number > reverseofnumber)
    {
        result = number - reverseofnumber;
    }
    else
    {
        result = reverseofnumber - number;
    }
    if (result % 9 == 0)
    {
        printf("%d is multiple of 9", result);
    }
    else
    {
        printf("%d is not divisible by 9", result);
    }
    return 0;
}