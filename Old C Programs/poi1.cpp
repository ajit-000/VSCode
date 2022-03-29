//basics of pointers

#include<stdio.h>
int main()
{
	int *a, x=10;
	a=&x;
	printf("Here we will find the address of the variable 'x'");
	printf("\n\nThe address of x is : %u ",a);
	/*if we'll take *a in printf the 
	the value at the address of a is printed*/
	return 0;
}
