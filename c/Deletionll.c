#include <stdio.h>
#include <stdlib.h>

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

struct Void *DeletionAtStart(struct Void *first)
{
    first = first->next;
    return first;
}

struct Void *DeletionAtLast(struct Void *first)
{
    struct Void *ptr1 = first;
    struct Void *ptr2 = first->next;

    while (ptr2->next != NULL)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    ptr1->next = NULL;
    free(ptr2);
    return first;
}

struct Void *DeletionInBetween(struct Void *first, int index)
{
    struct Void *ptr1 = first;
    struct Void *ptr2 = first->next;
    int i = 0;
    while (i < index - 1)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
        i++;
    }
    ptr1->next = ptr2->next;
    free(ptr2);
    return first;
}

struct Void *deleteAtIndex(struct Void *first, int value)
{
    struct Void *p = first;
    if (value == p->val)
    {
        first = first->next;
        return first;
    }

    struct Void *q = first->next;
    while (q->val != value && q->next != NULL)
    {
        p = p->next;
        q = q->next;
    }

    if (q->val == value)
    {
        p->next = q->next;
        free(q);
    }
    return first;
}

int main()
{
    struct Void *first;
    struct Void *second;
    struct Void *third;
    struct Void *fourth;
    int n1, n2, n3, n4, index, value;

    first = (struct Void *)malloc(sizeof(struct Void));
    second = (struct Void *)malloc(sizeof(struct Void));
    third = (struct Void *)malloc(sizeof(struct Void));
    fourth = (struct Void *)malloc(sizeof(struct Void));

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

    printf("The elements before deletion : \n");
    traverse(first);

    // printf("The elements after deletion : \n");
    // traverse(DeletionAtStart(first));

    // printf("The elements after deletion : \n");
    // traverse(DeletionAtLast(first));

    // printf("Enter the index at which you have to delete : ");
    // scanf("%d", &index);
    // traverse(DeletionInBetween(first, index - 1));

    printf("Enter the value which you have to delete : ");
    scanf("%d", &value);
    traverse(deleteAtIndex(first, value));

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}