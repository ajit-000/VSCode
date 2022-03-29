#include<stdio.h>
int main()
{
	int a,i,x=0;
	printf("enter the number \n");  //to check prime
	scanf("%d",&a);
	for(i=2;i<=a/2;i++)
	{
		if(a%i==0)
		{
			printf("%d is not prime number",a);
			goto p;
		}
	}
	if(a==1)
	{
		printf("1 is not considered as prime number");
	}
	else
	{
		printf("%d is prime number",a);
	}
	p:
		{
			return 0;
		}
}
