#include<stdio.h>

typedef union movie
{
    int a;
    float b;
    char c;
    double d;
} uno;
uno x,y,z;

int main()
{
    printf("The size of int is %d\n",__SIZEOF_INT__);
    printf("The size of float is %d\n",__SIZEOF_FLOAT__);
    printf("The size of union is %d",sizeof(uno));
    return 0;
}
