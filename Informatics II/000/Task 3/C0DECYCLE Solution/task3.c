#include <stdio.h>

int n = 7;
int A[] = {2, 45, 16, 2, 6, 33, 8};

int main() {
    int a = 0;
    int b = 0;

    for (int i = 0; i < n; i++) {
        if (A[i] > a) {
            b = a;
            a = A[i];
        } else if (A[i] > b) {
            b = A[i];
        }
    }

    printf("%d\n", b);
}