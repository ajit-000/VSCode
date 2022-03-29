#include<stdio.h>
int add(int a)
{
	if(a!=0)
	return a+add(a-1);
	else
	return a;
}
int main()
{
	int a;
	printf("enter the number :\n");
	scanf("%d",&a);
	printf("the addition till %d is : %d",a,add(a));
	return 0;	
}
