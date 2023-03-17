#include <stdio.h>

void pyramid(int A[], int n){
    if (n == 0) {
        return;
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
    for (int i = 0; i < n - 1; i++) {
        A[i] = A[i] + A[i + 1];
    }
    pyramid(A, n - 1);
}

int main(){
    int n = 5;
    int A[] = {5,4,6,1,3};
    pyramid(A, n);
    return 0;
}