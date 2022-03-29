//patterns in c
#include<stdio.h>
int main()
{
	int a,i,j;
	printf("how many rows do you want in an pyramid\n");
	scanf("%d",&a);
	for(i=0;i<=a;i++)
	{
		for(j=0;j<=i;j++)
		printf("*");
		printf("\n");
	}
	return 0;
}
