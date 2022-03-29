#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void traverse(struct Node *ptr)
{
    struct Node *first = ptr;
    do
    {
        printf("Element : %d\n", ptr->data);
        ptr = ptr->next;
    } while (ptr != first);
}

struct Node *insertionatstart(struct Node *first, int value)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = first->next;
    ptr->data = value;
    while (p->next != first)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->next = first;
    first = ptr;
    return first;
}

int main()
{
    struct Node *first;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    int n1, n2, n3, n4;
    int value;

    first = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    printf("Enter the first element : ");
    scanf("%d", &n1);
    first->data = n1;
    first->next = second;

    printf("Enter the second element : ");
    scanf("%d", &n2);
    second->data = n2;
    second->next = third;

    printf("Enter the first element : ");
    scanf("%d", &n3);
    third->data = n3;
    third->next = fourth;

    printf("Enter the first element : ");
    scanf("%d", &n4);
    fourth->data = n4;
    fourth->next = first;

    printf("\nCircular LL before insertion : \n");
    traverse(first);

    printf("\nEnter the value at which you have to insert at start : ");
    scanf("%d", &value);

    printf("\nCircular LL after insertion : \n");
    traverse(insertionatstart(first, value));

    free(first);
    free(second);
    free(third);
    free(fourth);

    return 0;
}