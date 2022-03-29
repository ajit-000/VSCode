//strings in c

#include<stdio.h>
int main()
{
	char a[20];
	printf("Enter the string : \n");
	fgets(a, sizeof(a), stdin);
	printf("\nThe string entered is :\n");
	puts(a);
	return 0;
}
