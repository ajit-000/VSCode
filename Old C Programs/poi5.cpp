#include<stdio.h>
int main()
{
	int a, arr[30], i;
	printf("Here we will print the addresses of ");
	printf("different locations of array using");
	printf(" different different types");
	printf("\n\nEnter the size of array\n");
	scanf("%d",&a);
	printf("\n\nEnter the elements is array :\n");
	for(i=0; i<a; i++)
	{
		scanf("%d",&arr[i]);
	}
	printf("The address of first element of array is : %d\n", &arr[0]);
	printf("The address of first element of array is : %d\n", arr);
	printf("The value of first element of array is : %d\n", *arr);
	printf("The value of first element of array is : %d\n\n", arr[0]);
	printf("The address of second element of array is : %d\n", &arr[1]);
	printf("The address of second element of array is : %d\n", arr+1);
	printf("The value of second element of array is : %d\n", arr[1]);
	printf("The value of second element of array is : %d\n", *(arr+1));
	return 0;
}
