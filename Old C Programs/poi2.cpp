#include<stdio.h>
int main()
{
	int *a, x;
	/* here we'll declare an pointer as [int* a=&x;] 
	this will works same as int *p, a; p=&a;*/
	printf("Enter the value to operate : \n");
	scanf("%d",&x);
	a=&x;
	printf("The updated value of 'x' is : %d",*a+1);
	/*here *a+1 and *(a+1) are totally different things
	because *a+1 symbolize the value at the address of 'x'
	and addition of 1 to it but.....
	*(a+1) symbolize the address of 'a' then addition of 
	1 to it*/
	return 0;
}
