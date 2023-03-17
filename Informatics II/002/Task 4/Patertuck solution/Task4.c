#include <stdio.h>

int A[] = {5,4,6,1,3};
int n = 5;

void drawTriangle(int A[], int n){
    int i;
    int B[n-1];

    // Condition to end recursion
    if (n==1){
        printf("%i\n", A[0]);
        return;        
    }

    // Form next uper level as an array
    for (i=0; i<n-1; i++){
        B[i] = A[i] + A[i+1];
    }

    drawTriangle(B, n-1);

    //print line of current level
    for (i=0; i<n; i++){
        printf("%i ", A[i]);
    }
    printf("\n");
}

int main(){
    drawTriangle(A, n);
    return 0;
}
