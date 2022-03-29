#include <stdio.h>
#include <string.h>

int main()
{
    char a[20],b[20],c[20];

    printf("Enter the first string :\n");
    fgets(a, sizeof(a),stdin);

    printf("Enter the second string :\n");
    fflush(stdin);
    fgets(b, sizeof(b),stdin);
    
    printf("\nString without swapping are :\n");
    puts(a);
    puts(b);

    strcpy(c,a);
    strcpy(a,b);
    strcpy(b,c);

    printf("\nThe swapped strings are :\n");
    puts(a);
    puts(b);

    return 0;
}
