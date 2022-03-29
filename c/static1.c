//recursion factorial program

#include<stdio.h>
int fact(int a)
{
    if (a>0)
    {
        return (a*fact(a-1));
    }
    else
    {
        return 1;
    }
}
int main()
{
    int a;
    printf("Enter the number : \n");
    scanf("%d",&a);
    fact(a);
    printf("\nThe factorial of %d is %d",a,fact(a));
    return 0;
}