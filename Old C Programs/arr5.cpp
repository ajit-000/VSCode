//copy the elements of arrayin second array

#include<stdio.h>
int main()
{
	int x,a1[20],a2[20],i,j;
	printf("enter the size of array : \n");
	scanf("%d",&x);
	
	printf("\nenter the elements of array :\n");
	
	for(i=1 ; i<=x ; i++)
	{
	scanf("%d",&a1[i]);
	a2[i]=a1[i];
	}
	
	printf("the elements of second array is : \n");
	
	for(j=1 ; j<=x ; j++)
	printf("%d\n",a2[j]);
	
	return 0;
}
