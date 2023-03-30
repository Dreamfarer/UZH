#include <stdio.h>

void swap(int *A, int i, int j)
{
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

void max_heapify(int *A, int n, int i, int d){
    int max_index = i;
    int max = A[max_index];

    for (int j = 1; j <= d & i * d + j < n; j++){
        int index = i * d + j;

        if (A[index] > max){
            max_index = index;
            max = A[max_index];
        }
    }

    if (max_index != i){
        swap(A, max_index, i);
        max_heapify(A, n, max_index, d);
    }

}
 

void buildMaxHeap(int *A, int n, int d){
    for (int i = (n - 1) / d; i >= 0; i--) {
        max_heapify(A, n, i, d);
    }
}

void printHeap(int A[], int n, int d) {
    printf("graph g {\n");

    for (int i = 0; i < n - 1; i++) {
        printf("  %d -- %d\n", A[i / d], A[i + 1]);
    }

    printf("}\n");
}

void heapSort(int *A, int n, int d) {
    buildMaxHeap(A, n, d);
    for (int i = n - 1; i >= 0; i--) {
        int temp = A[i];
        A[i] = A[0];
        A[0] = temp;
        max_heapify(A, i, 0, d);
    }
}

void printArray(int A[], int n) {
    printf("{");
    for (int i = 0; i < n; i++) {
        printf("%d", A[i]);
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf("}\n");
}

int main(){
    int n = 10;
    int A[] = {4, 3, 2, 5, 6, 7, 8, 9, 12, 1};
    int d = 3;

    buildMaxHeap(A, n, d);
    printHeap(A, n, d);
    heapSort(A, n, d);
    printArray(A, n);
}