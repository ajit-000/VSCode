#include <stdlib.h>
#include <stdio.h>

struct Void
{
    int val;
    struct Void *next;
};

void traverse(struct Void *ptr)
{
    while (ptr != NULL)
    {
        printf("Element : %d\n", ptr->val);
        ptr = ptr->next;
    }
}

struct Void *insertatbegining(struct Void *first, int element)
{
    struct Void *ptr = (struct Void *)malloc(sizeof(struct Void));
    ptr->val = element;
    ptr->next = first;
    return ptr;
}

struct Void *insertatmiddle(struct Void *first, int element, int index)
{
    struct Void *ptr = (struct Void *)malloc(sizeof(struct Void));
    struct Void *p = first;
    int i = 0;
    while (i != index - 1)
    {
        p = p->next;
        i++;
    }
    ptr->val = element;
    ptr->next = p->next;
    p->next = ptr;
    return first;
}

struct Void *insertatend(struct Void *first, int element)
{
    struct Void *ptr = (struct Void *)malloc(sizeof(struct Void));
    struct Void *p = first;
    while (p->next != NULL)
    {
        p = p->next;
    }
    ptr->val = element;
    p->next = ptr;
    ptr->next = NULL;
    return first;
}

int main()
{
    struct Void *first, *second, *third, *fourth;
    int n1, n2, n3, n4, element, index;
    first = (struct Void *)malloc(sizeof(struct Void));
    second = (struct Void *)malloc(sizeof(struct Void));
    third = (struct Void *)malloc(sizeof(struct Void));
    fourth = (struct Void *)malloc(sizeof(struct Void));

    printf("Enter the elements in array : \n");
    printf("Enter 1st element :");
    scanf("%d", &n1);
    first->val = n1;
    first->next = second;

    printf("Enter 2nd element :");
    scanf("%d", &n2);
    second->val = n2;
    second->next = third;

    printf("Enter 3rd element :");
    scanf("%d", &n3);
    third->val = n3;
    third->next = fourth;

    printf("Enter 4th element :");
    scanf("%d", &n4);
    fourth->val = n4;
    fourth->next = NULL;

    // printf("Enter the element you wants to enter at begining : ");
    // scanf("%d", &element);
    // traverse(insertatbegining(first, element));

    // printf("Enter the element you wants to enter at middle : ");
    // scanf("%d", &element);

    // printf("Enter the index at which you have to insert element :");
    // scanf("%d", &index);

    // traverse(insertatmiddle(first, element, index-1));

    // printf("Enter the number to insert at the end of the node : ");
    // scanf("%d", &element);

    // traverse(insertatend(first, element));

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}