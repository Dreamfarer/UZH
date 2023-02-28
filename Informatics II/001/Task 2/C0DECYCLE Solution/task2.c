#include <stdio.h>

#define DIM 2

int main() {
    int i, x, y, k;
    int mat[DIM * DIM];
    int matSqr[DIM * DIM];

    for (i = 0; i < DIM * DIM; i++) {
        scanf("%d", &mat[i]);
    }

    for (i = 0; i < DIM * DIM; i++) {
        matSqr[i] = mat[i] * mat[i];
    }

    for (i = 0; i < DIM * DIM; i++) {
        x = i % DIM;
        y = (i - x) / DIM;
        matSqr[i] = 0;
        for (k = 0; k < DIM; k++) {
            matSqr[i] += mat[y * DIM + k] * mat[k * DIM + x];
        }
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
