#include <stdlib.h>

struct Stack {
    int top;
    int max;
    int* array;
};

struct Stack* create(int max) {
    struct Stack* s = malloc(sizeof(struct Stack));
    s->top = -1;
    s->max = max;
    s->array = malloc(max * sizeof(int));
    return s;
}

void push(struct Stack* s, int value) {
    if (s->top == s->max - 1) {
        return;
    }
    s->array[++s->top] = value;
}

void pop(struct Stack* s) {
    if (s->top == -1) {
        return;
    }
    s->top--;
}