//programs to print the address of array

#include<stdio.h>
int main()
{
	int a[20],i,j,x;
	printf("enter the size of array :\n");
	scanf("%d",&x);
	printf("\nenter the elements in array\n");
	for(i=1;i<=x;i++)
	scanf("%d",&a[i]);
	printf("\nthe address of arrays are :\n");
	for(j=1;j<=x;j++)
	printf("%d\n",&a[j]);
	return 0;
}
