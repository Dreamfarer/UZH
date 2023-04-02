#include <stdio.h>

void swap(int *A, int i, int j)
{
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

int partition(int *A, int r, int l){

    if (A[l] > A[r]){
        swap(A, l, r);
    }

    int pivr = A[r];
    int i =-1;

    for (int j = 0; j < r; j++){
        if (A[j] <= pivr){
            i++;
            swap(A, i, j);
        }        
    }
    i++;
    swap(A, i, r);
    return (i);
}


void quicksort(int *A, int l, int r){

    if (l >= r){
        return;
    }

    int new_r = partition(A, r, l);
    int new_l = partition(A, new_r-1, 0);

    quicksort(A, 0, new_l - 1);
    quicksort(A, new_l, new_r - 1);
    quicksort(A, new_r + 1, r);
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
    int A[] = {9, 7, 2, 15, 8, 2, 8, 1, 17, 5};
    quicksort(A, 0, n-1);
    printArray(A, n);
}