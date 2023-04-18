#include <stdlib.h>

struct Node {
    int value;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

struct Node* createNode(int value) {
    struct Node* node = malloc(sizeof(struct Node));
    node->value = value;
    node->next = NULL;
    return node;
}

struct Stack* create() {
    struct Stack* s = malloc(sizeof(struct Stack));
    s->top = NULL;
    return s;
}

void push(struct Stack* s, int value) {
    struct Node* node = createNode(value);
    node->next = s->top;
    s->top = node;
}

void pop(struct Stack* s) {
    if (s->top == NULL) {
        return;
    }
    struct Node* temp = s->top;
    s->top = s->top->next;
    free(temp);
}