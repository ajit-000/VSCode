#include <stdio.h>
#include <stdlib.h>

struct list
{
    int val;
    struct list *next;
} * ptr;

void traverse(struct list *ptr)
{
    printf("\nThe elements of list are : \n");
    while (ptr != NULL)
    {
        printf("Element : %d\n", ptr->val);
        ptr = ptr->next;
    }
}

struct list *push(struct list *first)
{
    int num;
    printf("Enter the number you want to push in stack :");
    scanf("%d", &num);
    ptr = (struct list *)malloc(sizeof(struct list));
    ptr->val = num;
    ptr->next = first;
    return ptr;
}

struct list *pop(struct list *first)
{
    printf("\nThe popped element is : %d\n", first->val);
    first = first->next;
    return first;
}

int main()
{
    struct list *first, *second, *third, *fourth;
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

    traverse(push(first));

    traverse(pop(ptr));

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}