#include<stdio.h>
int fact(int a)
{
	if(a>=1)
	{
		return a*fact(a-1);
		
	}
	else
		return 1;
	
}
int main()
{
	int a;
	printf("enter the number for factorial\n");
	scanf("%d",&a);
	printf("the factorial of %d is %d",a,fact(a));
	return 0;	
}
