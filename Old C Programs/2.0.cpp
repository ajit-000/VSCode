//calculator using functions
#include<stdio.h>
int add(int x,int y)
{
	int c;
	c=x+y;
	printf("the addition of both numbers is %d",c);		
}
int sub(int x,int y)
{
	int c;
	c=x-y;
	printf("the substraction of both numbers is %d",c);
}
int mul(int x,int y)
{
	int c;
	c=x*y;
	printf("the multiplication of both numbers is %d",c);
}
int div(int x,int y)
{
	int c;
	c=x/y;
	printf("the division of both numbers is %d",c);
}
int main()
{
	int a,x,y;
	printf("choose any of the operands :\n");
	printf("for'+'-> press 1\nfor'-' -> press 2\n");
	printf("press 3 for ->'%'\n,press 4 for ->'*'\n");
	scanf("%d",&a);
	if(a==1)
	{
	printf("enter the numbers to add\n");
	scanf("%d%d",&x,&y);
	add(x,y);	
	}
	if(a==2)
	{
	printf("enter the numbers for substraction\n");
	scanf("%d%d",&x,&y);
	sub(x,y);	
	}
	if(a==3)
	{
	printf("enter the numbers to div\n");
	scanf("%d%d",&x,&y);
	add(x,y);	
	}
	if(a==4)
	{
	printf("enter the numbers to multiply\n");
	scanf("%d%d",&x,&y);
	mul(x,y);	
	}
	return 0;
}
