#include <stdio.h>
#include <stdlib.h>
#define N 10

struct node {
    int key;
    struct node* next;
};

struct node* convertArraytoLinkedList(int *arr, int n){
    struct node* root = malloc(sizeof(struct node));
    root->key = *arr;
    root->next = NULL;
    struct node* last = root;

    for (int i = 1; i < N; i++){
        struct node* current = malloc(sizeof(struct node));
        current->key = *(arr + i);
        current->next = NULL;
        last->next = current;
        last = current;
    }
    return root;    
}

void print(struct node* current) {
    
    while (current != NULL) {
        printf("%d ", current->key);
        current = current->next;
    }
}

struct node* reverseLinkedList(struct node* head){
    struct node* previous = NULL;
    struct node* current = head;

    while (current != NULL){
        struct node* temp = current->next;
        current->next = previous;
        previous = current;
        current = temp;
    }
    return previous;   
}

int main() {
    /* Generating an array of N random integers */
    int *arr;
    arr = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        *(arr + i) = rand();
    }

    struct node *head = convertArraytoLinkedList(arr, N);
    printf("The original: ");
    print(head);
    
    struct node* newHead = reverseLinkedList(head);
    printf("\nThe reversed: ");
    print(newHead);

    return 1;
}