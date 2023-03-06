#include <stdio.h>
#include <limits.h>

int A[] = {2, 45, 16, 2, 6, 33, 31};

int main() {
    int len = sizeof(A)/sizeof(A[0]);
    int largest = INT_MIN;
    int second = INT_MIN;

    for (int i = 0; i < len; i++){
        if (A[i]> largest){
            second = largest;
            largest = A[i];
        }
        else if (A[i] > second){
            second = A[i];
        }

    }
    printf("Second largest number of A: %d \n", second);
}