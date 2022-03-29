//armstrong number
#include<stdio.h>
#include<math.h>
int main()
{
	int a,x,p=0,q=0,r;
	printf("enter the number to check pallindrom\n");
	scanf("%d",&a);
	x=a;
	while(a!=0)
	{
		p=p+1;
		a=a/10;
	}
	a=x;
	while(a!=0)
	{
		r=a%10;
		q=q+pow(r,p);
		a=a/10;
	}
	printf("\n%d\n",q);
	if(x==q)
	{
		printf("%d is armstrong number",x);
	}
	else
	{
		printf("%d is not armstrong number",x);
	}
	return 0;
}
