#include<stdio.h>
struct driver
{
    char name[20];
    char dlno[20];
    char route[30];
    int kms;
}d1,d2,d3;

int main()
{
    printf("\n Enter the details of first driver :\n");
    printf("Enter the name :\n");
    scanf("%s",&d1.name);

    printf("Enter the dlno :\n");
    scanf("%s",&d1.dlno);

    printf("Enter the route :\n");
    scanf("%s",&d1.route);

    fflush(stdin);

    printf("Enter the kms :\n");
    scanf("%d",&d1.kms);

    printf("\n Enter the details of second driver :\n");

    printf("Enter the name :\n");
    scanf("%s",&d2.name);

    printf("Enter the dlno :\n");
    scanf("%s",&d2.dlno);

    printf("Enter the route :\n");
    scanf("%s",&d2.route);

    fflush(stdin);

    printf("Enter the kms :\n");
    scanf("%d",&d2.kms);

    printf("\n Enter the details of third driver :\n");

    printf("Enter the name :\n");
    scanf("%s",&d3.name);

    printf("Enter the dlno :\n");
    scanf("%s",&d3.dlno);

    printf("Enter the route :\n");
    scanf("%s",&d3.route);

    fflush(stdin);

    printf("Enter the kms :\n");
    scanf("%d",&d3.kms);

    printf("\n\n*************************************************\n");
    printf("For details :\n1.\tFor driver 1\n");
    printf("2.\tFor driver 2\n3.\tFor driver 3\n");
    int x;
    scanf("%d",&x);
    if(x==1)
    {
        printf("Name : %s\n",d1.name);
        printf("dlno : %s\n",d1.dlno);
        printf("route : %s\n",d1.route);
        printf("kms : %d\n",d1.kms);
    }

    else if(x==2)
    {
        printf("Name : %s\n",d2.name);
        printf("dlno : %s\n",d2.dlno);
        printf("route : %s\n",d2.route);
        printf("kms : %d\n",d2.kms);
    }

    else if(x==3)
    {
        printf("Name : %s\n",d3.name);
        printf("dlno : %s\n",d3.dlno);
        printf("route : %s\n",d3.route);
        printf("kms : %d\n",d3.kms);
    }

    else
    {
        printf("\nEnter the valid number");
    }

    return 0;
}