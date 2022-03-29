#include <stdio.h>
#include <stdlib.h>

struct list
{
    int val;
    struct list *next;
};

void traverse(struct list *ptr)
{
    while (ptr != NULL)
    {
        printf("Element : %d\n", ptr->val);
        ptr = ptr->next;
    }
}

int main()
{
    struct list *first;
    struct list *second;
    struct list *third;
    struct list *fourth;
    int n1, n2, n3, n4;

    first = (struct list *)malloc(sizeof(struct list));
    second = (struct list *)malloc(sizeof(struct list));
    third = (struct list *)malloc(sizeof(struct list));
    fourth = (struct list *)malloc(sizeof(struct list));

    printf("Enter the value of first element : ");
    scanf("%d", &n1);
    first->val = n1;
    first->next = second;

    printf("Enter the value of second element : ");
    scanf("%d", &n2);
    second->val = n2;
    second->next = third;

    printf("Enter the value of third element : ");
    scanf("%d", &n3);
    third->val = n3;
    third->next = fourth;

    printf("Enter the value of fourth element : ");
    scanf("%d", &n4);
    fourth->val = n4;
    fourth->next = NULL;

    traverse(first);

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}