// largest and second largest number in array

#include<stdio.h>
int main()
{
	int x, a[20], i, j, k, y;
	printf("enter the size of array : \n");
	scanf("%d",&x);
	printf("\nenter the elements of array :\n");
	for(i=0; i<x ; i++)
	scanf("%d",&a[i]);
	for(j=0 ;j<x ;j++)
	{
		for(k=j+1; k<x; k++)
		if(a[j]<a[k])
	{
		y = a[j];
		a[j] = a[k];
		a[k] = y;
	}
	}
	printf("\nthe largest number of this array is : %d\n",a[0]);
	printf("\nthe second largest number of this array is : %d\n",a[1]);
	return 0;
}
