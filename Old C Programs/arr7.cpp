//sorting an array

#include<stdio.h>
int main ()
{
    int i, j, k, a[20], x, y;
    printf("enter the size of array : \n");
    scanf("%d",&x);
    printf("\nenter the elements in array : \n");
    
    for(i=0; i<x; i++)
    scanf("%d",&a[i]);
    
    for(j=0; j<x; j++)
    {    
        for(k=j+1; k<x; k++) 
        {    
            if(a[k] > a[j])    
            {    
                y = a[j];
                a[j] = a[k];
                a[k] = y;
            }
        }
    }
    printf("Printing Sorted Element List :\n");
    for(j=0; j<x; j++)
    {
        printf("%d\n",a[j]);
    }
    return 0;
}
