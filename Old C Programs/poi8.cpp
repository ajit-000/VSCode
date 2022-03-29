//pointers to swap

#include<stdio.h>

int swap(int* a,int* b)
{
	int x;
	x=*a;
	*a=*b;
	*b=x;
}

int main()
{
	int a, b, x;
	printf("Enter the first value :\na=");
	scanf("%d",&a);
	printf("\nEnter the second value :\nb=");
	scanf("%d",&b);
	swap(&a,&b);
	printf("the swapped values are :\na=%d\tb=%d",a,b);
}
