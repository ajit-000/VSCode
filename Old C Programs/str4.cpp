#include<stdio.h>
#include<string.h>
int main()
{
	char a[30];
	int x;
	printf("Enter your string : \n");
	fgets(a, sizeof(a), stdin);
	printf("The string you entered is : \n");
	puts(a);
	printf("To convert your string :\n");
	printf("Press 1 for uppercase\n");
	printf("Press 2 for lowercase\n");
	printf("Press 3 to reverse the string\n\n");
	scanf("%d",&x);
	if(x==1)
	{
		strupr(a);
		printf("The string you want is :\n");
		puts(a);
	}
	
	else if(x==2)
	{
		strlwr(a);
		printf("The string you want is :\n");
		puts(a);
	}
	
	else if(x==3)
	{
		strrev(a);
		printf("the reverse of that string is : \n");
		puts(a);
	}
	
	else
	printf("please give a valid input");
	return 0;
}
