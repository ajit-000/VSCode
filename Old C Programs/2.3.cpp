//prime num. between a given range
//WITHOUT USING FUNCTIONS

#include<stdio.h>
int main()
{
	int a,b,i,j,x,count =0,p;
	printf("Enter the first number\n");
	scanf("%d",&a);
	if(a<2)
	{
		printf("The value you entered for first digit is less than 2\n");
		printf("So,we'll update your value to '2' for ease\n\n ");
		a=2;
	}
	printf("Enter the second number\n");
	scanf("%d",&b);
	if(b<2)
	{
		printf("The value you entered for second digit is less than 2\n");
		printf("We'll update your value to '2' for ease ");
		b=2;
	}
	else if(a==b)
	{
		printf("Both number entered are equal \n");
		printf("So their is no prime number in between \n");
		goto p;
	}
	else if(a>b)
	{
		a=a+b;
		b=a-b;
		a=a-b;
	}	
	printf("The prime numbers between %d and %d are : \n",a,b);
	for(i=a;i<=b;i++)
	{
		for(j=2;j<=i/2;j++)
		{
			x=0;
			if(i%j == 0)
			{
				x=1;
				break;
			}
		}
		if(x==0)
		{
			printf("%d\n",i);
			count ++;
		}
	}
	printf("\nThe prime numbers between %d and %d are %d",a,b,count);
	p :
	{
	return 0;
	}
}
