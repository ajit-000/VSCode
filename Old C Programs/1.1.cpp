//program for calculator via switch

#include<stdio.h>
#include<conio.h>
int main()
{
	int a,b,c;
	char op;
	X :{
	printf("Enter the operator e.g. +,-,/,*\n");
	scanf("%c",&op);
	printf("Enter two operands\n");
	scanf("%d%d",&a,&b);
	switch(op){
		case '+':
		printf("The addition of %d and %d is %d",a,b,a+b);
		break;
		case '-':
		printf("The substraction of %d and %d is %d",a,b,a-b );	
		break;
		case '*':
		printf("The multiplication of %d and %d is %d",a,b,a*b);
		break;
		case '/':
		printf("The division of %d and %d is %d",a,b,a/b);
		break;
		default :
		printf("Invalid syntax");
}
printf("\nIf you want to perform the operations again....\n press '1' \n press else '0'\n");
scanf("%d",&c);
if(c==1)
{
goto X;
getch();
}
else
return 0;

}
}
