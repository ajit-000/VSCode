#include<stdio.h>

int main()
{
	int arr[30], i, x, sum=0;
	
	printf("Enter the size of array :\n");
	scanf("%d",&x);
	
	printf("Enter the elements in array :\n");
	
	for(i=0; i<x; i++)
	{
		scanf("%d",arr+i);
		sum += *(arr+i);
	}
	
	printf("The sum of all the elements of array is : %d",sum);
	
	return 0;
}
