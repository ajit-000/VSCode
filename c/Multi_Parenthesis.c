#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    char *arr;
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(struct stack *ptr, char val)
{
    if (isFull(ptr))
    {
        printf("Stack Overflow! Cannot push %d to the stack\n", val);
    }
    else
    {
        ptr->top++;
        ptr->arr[ptr->top] = val;
    }
}

char pop(struct stack *ptr)
{
    if (isEmpty(ptr))
    {
        printf("Stack Underflow! Cannot pop from the stack\n");
        return 0;
    }
    else
    {
        char val = ptr->arr[ptr->top];
        ptr->top--;
        return val;
    }
}

int match(char char1, char char2)
{
    if (char1 == '(' && char2 == ')' || char1 == '[' && char2 == ']' || char1 == '{' && char2 == '}')
    {
        return 1;
    }
    return 0;
}

int isMatching(char *ptr)
{
    struct stack *s;
    s->size = 80;
    s->top = -1;
    s->arr = (char *)malloc(s->size * sizeof(int));

    for (int i = 0; ptr[i] != '\0'; i++)
    {
        char elem;
        if (ptr[i] == '(' || ptr[i] == '{' || ptr[i] == '[')
        {
            push(s, ptr[i]);
        }
        else if (ptr[i] == ')' || ptr[i] == '}' || ptr[i] == ']')
        {
            if (isEmpty(s))
            {
                return 0;
            }
            elem = pop(s);
            if (!match(elem, ptr[i]))
            {
                return 0;
            }
        }
    }
    if (isEmpty(s))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    char *exp = "[{()}()]";
    if (isMatching(exp))
    {
        printf("The parenthesis are Matching");
    }
    else
    {
        printf("The parenthesis are not Matching");
    }
    return 0;
}
