//loops programs

#include<stdio.h>
int main()
{
	int a,i,x=0;
	printf("enter the last digit till you want to print numbers\n");
	scanf("%d",&a);
	for(i=0;i<=a;i++)
	{
		printf("%d\n",i);
		x=x+i;
	}
	printf("\nthe sum of numbers is %d",x);
	return 0;
}
