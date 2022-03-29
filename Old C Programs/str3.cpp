#include<stdio.h>
#include<string.h>
#include<conio.h>
char len(char a[])
{
	printf("the length of your string is : %d\n",strlen(a));
}
char con(char a[])
{
	char b[50];
	printf("\nEnter the second string to concatinate :\n");
	/*since pointer takes the ascii value of enter 
	and perform operation on it
	so by fflush well hold it*/
	fflush(stdin);
	fgets(b , sizeof(b), stdin);
	printf("The new strin is : \n");
	strcat(a,b);
	puts(a);
}
char cpy(char a[])
{
	char b[50];
	printf("the new string is : \n");
	strcpy(b,a);
	puts(b);
	
}
char comp(char a[])
{
	char b[50];
	printf("\nEnter the second string to compare :\n");
	fflush(stdin);
	fgets(b , sizeof(b), stdin);
	printf("The new strin is : \n");
	printf("the difference between two strind are %d",strcmp(a,b));
}
int main()
{
	int x;
	char a[50];
	printf("\n\tWelcome to string handling\n");
	printf("********************************************\n");
	printf("\nHere you will perform the operation on string\n");
	printf("\nEnter your string : \n");
	fgets(a, sizeof(a), stdin);
	printf("\nPress 1 to get length of your string\n");
	printf("\nPress 2 to concatinate your string\n");
	printf("\nPress 3 to add your string\n");
	printf("\nPress 4 to compare your string\n");
	scanf("%d",&x);
	if(x==1)
	{
		len(a);
	}
	else if(x==2)
	{

		con(a);
	}
	else if(x==3)
	{
		cpy(a);
	}
	else
	{
		comp(a);
	}
	
	return 0;
}
