#include<stdio.h>
int main()
{
	int a,i,j;
	printf("enter the rows for pyramid\n");
	scanf("%d",&a);
	for(i=0;i<=a;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%d ",j);
		}
		printf("\n");
	}
	return 0;
}
