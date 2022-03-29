//full pyramid
#include<stdio.h>
int main()
{
	int a,i,j,k;
	printf("enter the rows for pyramid\n");
	scanf("%d",&a);
	printf("the pattern for this pyramid is :\n\n");
	for(i=1;i<=a;i++)
	{
		for(j=1;j<=a-i;j++)
		{
			printf(" ");
		}
		for(k=i;k<=2*i-1;k++)
		{
			printf("* ");
		}
		printf("\n");
	}
	return 0;
}
