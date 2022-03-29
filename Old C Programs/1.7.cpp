#include<stdio.h>
int main()
{
	int a,i,j;
	char c='A';
	printf("enter the rows for pyramid\n");
	scanf("%d",&a);
	for(i=0;i<=a;i++)
	{
		for(j=0;j<=i;j++)
		{
			printf("%c ",c);
		}
		printf("\n");
		c=c+1;
	}
	return 0;
}
