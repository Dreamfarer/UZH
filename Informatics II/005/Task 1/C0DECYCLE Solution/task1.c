#include <stdio.h>

void heapify(int A[], int n, int i, int d) {
    int indices[d + 1];
    while (1) {
        for (int j = 1; j <= d; j++) {
            int index = d * i + j;
            indices[j] = index < n ? index : -1;
        }
        int maxChild = -1;
        int maxChildIndex;
        for (int j = 1; j <= d; j++) {
            int index = indices[j];
            if (index != -1 && A[index] > maxChild) {
                maxChildIndex = index;
                maxChild = A[index];
            }
        }
        if (maxChild == -1) {
            break;
        }
        if (A[i] < A[maxChildIndex]) {
            int temp = A[i];
            A[i] = A[maxChildIndex];
            A[maxChildIndex] = temp;
        }
        i = maxChildIndex;
    }
}

void buildMaxHeap(int A[], int n, int d) {
    for (int i = (n - 1) / d; i >= 0; i--) {
        heapify(A, n, i, d);
    }
}

void heapSort(int A[], int n, int d) {
    buildMaxHeap(A, n, d);
    for (int i = n - 1; i >= 0; i--) {
        int temp = A[i];
        A[i] = A[0];
        A[0] = temp;
        heapify(A, i, 0, d);
    }
}

void printHeap(int A[], int n, int d) {
    printf("graph g {\n");
    for (int i = 0; i < n - 1; i++) {
        printf("  %d -- %d\n", A[i / d], A[i + 1]);
    }
    printf("}\n");
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

int main() {
    int n = 12;
    int A[] = {6, 4, 3, 9, 5, 10, 15, 19, 11, 7, 8, 13};
    int d = 3;

    buildMaxHeap(A, n, d);
    printHeap(A, n, d);
    heapSort(A, n, d);
    printArray(A, n);
}