#include <stdio.h>
#include <stdlib.h>

#define N 10

struct node {
    int key;
    struct node* next;
};

struct node* convertArrayToLinkedList(const int* arr, int n) {
    struct node* root = malloc(sizeof(struct node));
    root->key = *(arr);
    root->next = NULL;
    struct node* previous = root;
    for (int i = 1; i < n; i++) {
        struct node* element = malloc(sizeof(struct node));
        element->key = *(arr + i);
        element->next = NULL;
        previous->next = element;
        previous = element;
    }
    return root;
}

void print(struct node* curr) {
    while (curr != NULL) {
        printf("%d ", curr->key);
        curr = curr->next;
    }
}

struct node* reverseLinkedList(struct node* head) {
    struct node* previous = NULL;
    struct node* current = head;
    while (current != NULL) {
        struct node* next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }
    return previous;
}

int main() {
    int* arr = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        *(arr + i) = i;
    }

    struct node* head = convertArrayToLinkedList(arr, N);
    printf("The original: ");
    print(head);

    struct node* newHead = reverseLinkedList(head);
    printf("\nThe reversed: ");
    print(newHead);
}
