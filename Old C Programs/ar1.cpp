//take array from user and print it

#include<stdio.h>
int main()
{
int a[50],i,j,x;
printf("how many elements do you want in array : \n");
scanf("%d",&x);
printf("enter the numbers in the array : \n");
for(i=1;i<=x;i++)
scanf("%d",&a[i]);
printf("\nthe elements of the array are as follows:\n");
for(j=1;j<=x;j++)
printf("%d\n",a[j]);
return 0;
}
