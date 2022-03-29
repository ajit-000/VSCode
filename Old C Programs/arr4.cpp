//reverse the array

#include<stdio.h>
int main()
{
	int x,a[20],i,j;
	printf("enter the size of array : \n");
	scanf("%d",&x);
	
	printf("\nenter the elements of array :\n");
	
	for(i=1 ; i<=x ; i++)
	scanf("%d",&a[i]);
	
	printf("the reverse of this array is : \n");
	
	for(j=x ; j>=1 ; j--)
	printf("%d\n",a[j]);
	
	return 0;
}
