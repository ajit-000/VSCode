#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *previous;
    struct Node *next;
};

void traverse_normal(struct Node *first)
{
    struct Node *ptr = first;
    do
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    } while (ptr != NULL);
}

void traverse_reversed(struct Node *fourth)
{
    struct Node *ptr = fourth;
    printf("\nThe Reversed Linked List is :\n");
    do
    {
        printf("%d ", ptr->data);
        ptr = ptr->previous;
    } while (ptr != NULL);
}

struct Node *insertion_begining(struct Node *first, int value)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = value;
    ptr->next = first;
    ptr->previous = NULL;
    first->previous = ptr;
    first = ptr;
    return first;
}

struct Node *insertion(struct Node *first, int value, int index_value)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = first;
    while (p->data != index_value)
    {
        p = p->next;
    }
    ptr->data = value;
    ptr->next = p->next;
    ptr->previous = p->previous;
    p->next = ptr;
    ptr = p;
    return first;
}

int main()
{
    struct Node *first, *second, *third, *fourth;
    int n1, n2, n3, n4, value, index_value;

    first = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    printf("Enter the first element : ");
    scanf("%d", &n1);
    first->data = n1;
    first->previous = NULL;
    first->next = second;

    printf("Enter the second element : ");
    scanf("%d", &n2);
    second->data = n2;
    second->previous = first;
    second->next = third;

    printf("Enter the third element : ");
    scanf("%d", &n3);
    third->data = n3;
    third->previous = second;
    third->next = fourth;

    printf("Enter the fourth element : ");
    scanf("%d", &n4);
    fourth->data = n4;
    fourth->previous = third;
    fourth->next = NULL;

    printf("Circular LL before insertion :\n");
    traverse_normal(first);

    printf("\nEnter the value you have to insert : ");
    scanf("%d", &value);

    printf("Enter the value after which you have to insert : ");
    scanf("%d", &index_value);

    printf("Circular LL after insertion :\n");
    // traverse_normal(insertion_begining(first, value));
    traverse_normal(insertion(first, value, index_value));

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}