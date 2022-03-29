#include<stdio.h>

typedef struct height
{
    char name[20];
    int f;    //for foots
    int i;  //for inch
} hei;

hei a1,a2;

int main()

{
    printf("\n\tProgram to add heights of persons\n");
    printf("**********************************************************\n\n");

    printf("Enter the name of first person :\n");
    scanf("%s",&a1.name);

    printf("\nEnter the height of first person :\n");
    printf("FOOTS : ");
    scanf("%d",&a1.f);

    printf("INCH : ");
    scanf("%d",&a1.i);

    printf("\nEnter the name of second person :\n");
    scanf("%s",&a2.name);

    printf("\nEnter the height of second person :\n");
    printf("FOOTS : ");
    scanf("%d",&a2.f);
    
    printf("INCH : ");
    scanf("%d",&a2.i);
    int x,y;

    x= a1.f+a2.f;
    y=a1.i+a2.i;

    while(y>12)
    {
        y = y-12 ;
        x++;
    }

    printf("\n\nThe sum of heights are : %d'%d\n",x,y);
    printf("\n\t\tor\n\n");
    printf("The sum of heights are : %d foot %d inch\n\n",x,y);
    return 0;
}