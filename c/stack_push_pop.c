#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

int isempty(struct stack *a)
{
    if (a->top == -1)
    {
        // printf("The stack is Empty");
        return 1;
    }
    else
    {
        // printf("The stack is not Empty");
        return 0;
    }
}

int isfull(struct stack *a)
{
    if (a->top == a->size - 1)
    {
        // printf("The stack is full");
        return 1;
    }
    else
    {
        // printf("The stack is not full");
        return 0;
    }
}

struct stack *push_elem(struct stack *new_s, int element)
{
    if (isfull(new_s))
    {
        printf("Stack Overflow\nNew Element cannot be stored");
        return new_s;
    }
    else
    {
        new_s->top++;
        new_s->arr[new_s->top] = element;
        return new_s;
    }
}

int pop_elem(struct stack *new_s)
{
    if (isempty(new_s))
    {
        printf("Stack Underflow\nNo element left");
    }
    else
    {
        int val = new_s->arr[new_s->top];
        new_s->top--;
        return val;
    }
}

int main()
{
    int sz, element1, element2, element3, element4, element5;
    struct stack *s = (struct stack *)malloc(sizeof(struct stack));

    printf("Enter the size of array you want to create : ");
    scanf("%d", &sz);
    s->size = sz;
    s->top = -1;

    s->arr = (int *)malloc(s->size * (sizeof(int)));

    printf("Enter element 1: ");
    scanf("%d", &element1);
    push_elem(s, element1);

    printf("Enter element 2: ");
    scanf("%d", &element2);
    push_elem(s, element2);

    printf("Enter element 3: ");
    scanf("%d", &element3);
    push_elem(s, element3);

    printf("Enter element 4: ");
    scanf("%d", &element4);
    push_elem(s, element4);

    printf("Enter element 5: ");
    scanf("%d", &element5);
    push_elem(s, element5);

    for (int i = 0; i <= s->top; i++)
    {
        printf("The value at %d position is %d\n", i, s->arr[i]);
    }

    printf("\nThe top value of stack is : %d", s->arr[s->top]);
    printf("\nThe last value of stack is : %d", s->arr[0]);

    printf("\n\nPopping out elements from stack : \n");
    printf("The first element popped is : %d\n", pop_elem(s));
    printf("The second element popped is : %d\n", pop_elem(s));
    printf("The third element popped is : %d\n", pop_elem(s));

    printf("\n**************************************************************\n");
    printf("Here we observe the L.I.F.O (last in first out) manner of list");
    printf("\n**************************************************************\n");

    return 0;
}