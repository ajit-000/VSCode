#include<stdio.h>
int add(int arr[30], int x)
{
	int i, j;
	printf("The addition to each elements of array is :\n");
	for(i=0; i<x; i++)
	{
		arr[i] = arr[i]+1;
	}
	
	for(j=0; j<x; j++)
	{
		printf("%d\n",*(arr+j));
	}
}

int main()
{
	int arr[30], i, j, x;
	printf("Enter the size of array  :\n");
	scanf("%d",&x);
	printf("Enter the elements in array :\n");
	for(i=0; i<x; i++)
	{
		scanf("%d",&arr[i]);
	}
	printf("The elements of array are : \n");
	for(j=0; j<x; j++)
	{
		printf("%d\n",*(arr+j));
	}
	add(arr,x);
	
	return 0;
}
