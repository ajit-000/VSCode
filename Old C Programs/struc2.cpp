#include<stdio.h>

struct person
{
	char name[30];
	int age;
	int salary;
} a1, a2, a3;

int main()
{
	printf("\t\tBASIC STRUCTURE PROGRAM\n");
	printf("\t********************************************\n\n");
	
	printf("Enter the detail of first person :\nName :\t");
	scanf("%s",&a1.name);
	
	printf("Age :\t");
	scanf("%d",&a1.age);
	
	printf("Salary :\t");
	scanf("%d",&a1.salary);
	
	printf("\n\t********************************************\n\n");
	
	printf("Enter the detail of second person :\nName :\t");
	scanf("%s",&a2.name);
	
	printf("Age :\t");
	scanf("%d",&a2.age);
	
	printf("Salary :\t");
	scanf("%d",&a2.salary);
	
	printf("\t********************************************\n\n");
	
	printf("Enter the detail of third person :\nName :\t");
	scanf("%s",&a3.name);
	
	printf("Age :\t");
	scanf("%d",&a3.age);
	
	printf("Salary :\t");
	scanf("%d",&a3.salary);
	
	int x;
	
	printf("\nTo view the profile of members:\n");
	printf("Press 1 For a1\nPress 2 For a2\n");
	printf("Press 3 For a3\n");
	printf("Enter your choice :\n");
	scanf("%d",&x);
	
	if(x==1)
	{
		printf("\nNAME : %s",a1.name);
		printf("\nAGE : %d",a1.age);
		printf("\nSALARY : %d",a1.salary);
	}
	
	else if(x==2)
	{
		printf("\nNAME : %s",a2.name);
		printf("\nAGE : %d",a2.age);
		printf("\nSALARY : %d",a2.salary);
	}
	
	else if(x==3)
	{
		printf("\nNAME : %s",a3.name);
		printf("\nAGE : %d",a3.age);
		printf("\nSALARY : %d",a3.salary);
	}
	
	else
	printf("Enter the valid number");
}
