#include <stdio.h>
#include <string.h>

int main()
{

    char str[30], words[30];
    int c = 0, d = 0;
    system("cls");
    printf("\nEnter the string:\n");
    gets(str);

    while (str[c] != '\0')
    {
        if (!(str[c] == ' ' && str[c + 1] == ' '))
        {
            words[d] = str[c];
            d++;
        }
        c++;
    }
    words[d] = '\0';
    printf("\nThe Desirable string is: %s", words);
    return 0;
}