#include <stdio.h>

#define DIM 2

int main() {
    int i, x, y;
    int mat[DIM * DIM];
    int matSqr[DIM * DIM];

    for (i = 0; i < DIM * DIM; i++) {
        scanf("%d", &mat[i]);
    }
    for (i = 0; i < DIM * DIM; i++) {
        matSqr[i] = mat[i] * mat[i];
    }

    for (y = 0; y < DIM; y++) {
        for (x = 0; x < DIM * 2; x++) {
            i = (x % DIM) + DIM * y;
            if (x < DIM) {
                printf("%d ", mat[i]);
            } else {
                printf("%d ", matSqr[i]);
            }
        }
        printf("\n");
    }

    return 0;
}
