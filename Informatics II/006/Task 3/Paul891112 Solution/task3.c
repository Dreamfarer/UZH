#include<stdio.h>
#include<stdlib.h>
#define N 10


struct node {
    int key;
    struct node* next;
};

struct node* convertArraytoLinkedList(int *arr, int n){

    struct node* root = malloc(sizeof(struct node));
    struct node* p = root;

    for(int i=0;i<n;i++){
        p->key = arr[i];
        if (i<n-1){//not final element, create next node and point there
            p->next = malloc(sizeof(struct node));
            p=p->next;
        }
        else{p->next = NULL;} //final element
    }
    return root;
}


void print(struct node* curr){

    struct node* p = curr;
    while(p->next != NULL){ 
        printf("%d, ",p->key);
        p=p->next;
    }
    printf("%d", p->key); 
    printf("\n");
}


struct node* reverseLinkedList(struct node* head){

    struct node* root = malloc(sizeof(struct node));
    struct node* p = root;

    //The linked list has zero or one element
    if(head == NULL || head->next == NULL){
        return head;
    }


    while(1){
        struct node* tail = head->next;
        struct node* prev = head;
         while(tail->next != NULL){ //until tail points at final element
            tail=tail->next;
            prev = prev->next;

        }
        if (prev == head){ //base case: two elements left
            p->key = tail->key;
            p->next = malloc(sizeof(struct node));
            p=p->next;
            free(tail);
            p->key = prev->key;
            p->next = NULL;
            free(prev);
            break;
        }

        //When there are more than two elemens left, aka prev != head
        p->key = tail->key;
        p->next = malloc(sizeof(struct node));
        p=p->next;
        prev->next = NULL;
        free(tail);
        
    }
   
    return root;
}



int main(){

    /* Generating an array of N random integers */
    int *arr;
    arr = malloc(N*sizeof(int));
    for (int i=0;i<N;i++){
        *(arr+i) = rand();
    }

    struct node* head = convertArraytoLinkedList(arr,N);

    printf("\nThe original: ");
    print(head);

    struct node* newHead = reverseLinkedList(head);

    printf("\nThe reversed: ");
    print(newHead);

    return 1;
}