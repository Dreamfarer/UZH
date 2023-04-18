#include <stdlib.h>

struct Node {
    int value;
    struct Node* next;
};

struct Queue {
    struct Node* front;
    struct Node* back;
};

struct Node* createNode(int value) {
    struct Node* node = malloc(sizeof(struct Node));
    node->value = value;
    node->next = NULL;
    return node;
}

struct Queue* create() {
    struct Queue* q = malloc(sizeof(struct Queue));
    q->front = NULL;
    q->back = NULL;
    return q;
}

void enqueue(struct Queue* q, int value) {
    struct Node* node = createNode(value);
    if (q->back == NULL) {
        q->front = node;
        q->back = node;
        return;
    }
    q->back->next = node;
    q->back = node;
}

void dequeue(struct Queue* q) {
    if (q->front == NULL) {
        return;
    }
    struct Node* node = q->front;
    q->front = q->front->next;
    if (q->front == NULL) {
        q->back = NULL;
    }
    free(node);
}