//strings in c

#include<stdio.h>
int main()
{
	char c[] = "my name is ram";
	//we'll not use scanf in strings
	//since it will stopped when any 
	//blankspace is encountered
	printf("the string you entered is : %s",c);
	return 0;
}
