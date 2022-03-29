// Program to find the average of n numbers using arrays

#include<stdio.h>
int main()
{
	int x,y=0,a[20],i,avr;
	printf("How many elements do you want in array : \n");
	scanf("%d",&x);
	printf("\nEnter the numbers :\n");
	for(i=1;i<=x;i++)
	{
	scanf("%d",&a[i]);
	y+=a[i];
	}
	avr=y/x;
	printf("\nThe average of all numbers is : %d",avr);
	return 0;
	
}
