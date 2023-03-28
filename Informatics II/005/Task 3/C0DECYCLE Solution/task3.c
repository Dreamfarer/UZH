#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int* A, int l, int h, int* lp) {
    if (A[l] > A[h]) {
        swap(&A[l], &A[h]);
    }
    int j = l + 1;
    int g = h - 1;
    int i = l + 1;
    int p = A[l];
    int q = A[h];
    while (i <= g) {
        if (A[i] < p) {
            swap(&A[i], &A[j]);
            j++;
        } else if (A[i] >= q) {
            while (A[g] > q && i < g) {
                g--;
            }
            swap(&A[i], &A[g]);
            g--;
            if (A[i] < p) {
                swap(&A[i], &A[j]);
                j++;
            }
        }
        i++;
    }
    j--;
    g++;
    swap(&A[l], &A[j]);
    swap(&A[h], &A[g]);
    *lp = j;
    return g;
}

void dualQuicksort(int* A, int l, int h) {
    if (l >= h) {
        return;
    }
    int lp;
    int rp;
    rp = partition(A, l, h, &lp);
    dualQuicksort(A, l, lp - 1);
    dualQuicksort(A, lp + 1, rp - 1);
    dualQuicksort(A, rp + 1, h);
}

void printArray(int A[], int n) {
    printf("[ ");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("]\n");
}

int main() {
    int n = 10;
    int A[] = {10, 7, 3, 15, 6, 2, 5, 1, 17, 8};

    printf("Before: ");
    printArray(A, n);
    dualQuicksort(A, 0, n - 1);
    printf("After: ");
    printArray(A, n);
}