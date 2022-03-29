//pascals triangle
#include<stdio.h>
int main()
{
	int a,i,j,x=0;
	printf("enter the rows for pyramid\n");
	scanf("%d",&a);
	for(i=0;i<=a;i++)
	{
		for(j=1;j<=i;j++)
		{
			x=x+1;
			printf("%d ",x);
		}
		printf("\n");
	}
	return 0;
}
