#include <stdlib.h>

struct Queue {
    int front;
    int back;
    int size;
    int max;
    int* array;
};

struct Queue* create(int max) {
    struct Queue* q = malloc(sizeof(struct Queue));
    q->front = 0;
    q->back = max - 1;
    q->size = 0;
    q->max = max;
    q->array = malloc(q->max * sizeof(int));
    return q;
}

void enqueue(struct Queue* q, int value) {
    if (q->size == q->max) {
        return;
    }
    q->back = (q->back + 1) % q->max;
    q->size = q->size + 1;
    q->array[q->back] = value;
}

void dequeue(struct Queue* q) {
    if (q->size == 0) {
        return;
    }
    q->front = (q->front + 1) % q->max;
    q->size = q->size - 1;
}