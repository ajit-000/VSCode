#include<stdio.h>

int main()
{
    int a=10;
    int *ptr=&a;
    int **q=ptr;
    printf("%d",*q);
    return 0;
}   