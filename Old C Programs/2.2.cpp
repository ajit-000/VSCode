// pallindrom number

#include<stdio.h>
int main()
{
	int a,x,t,rev=0;
	printf("enter any number :\n");
	scanf("%d",&a);
	x=a;
	while(a!=0)
	{
		t=a%10;
		rev=rev*10+t;
		a=a/10;	
	}
	if(rev==x)
		printf("the number is pallindrom");
	else
		printf("the number is not pallindrom");
	return 0;
}
