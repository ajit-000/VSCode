#include <stdio.h>
#include <stdlib.h>
int main()
{
    int num, i = 0;
    char *ptr;
    while (i < 3)
    {
        printf("Employee %d:\nEnter the number of characters in your Employee Id\n", i + 1);
        scanf("%d", &num);
        getchar(); 
        ptr = (char *)malloc((num + 1) * sizeof(char));
        printf("Enter your Employee Id\n");
        scanf("%s", ptr);
        getchar();
        printf("Your Employee Id is %s\n", ptr);
        free(ptr);
        i = i + 1;
    }

    return 0;
}