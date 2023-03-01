#include <stdio.h>

int main() {
    int dimension = 2;
    int matrix[dimension*dimension];
    int matrixsqr[dimension*dimension];
    int i, j, column, row_start;

    for (i=0; i<dimension * dimension; i++){
        scanf("%d", &matrix[i]);
    }
    //calculating matrixsqr
    for (i=0; i<dimension * dimension; i++){
        column = i % dimension;
        row_start = i - column;
        matrixsqr[i] = 0;

        for (j=0; j<dimension; j++){
            matrixsqr[i] += matrix[row_start + j] * matrix[j * dimension + column];
        }
    }

    //printing result, could probably be done smoother
    for (i=0; i<dimension * dimension + 1; i++){
        if (i % dimension == 0 & i != 0){
            for (j=0;j<dimension;j++){
                printf("%d ", matrixsqr[i-dimension+j]);
            }
            printf("\n");
            if (i==dimension*dimension){
                break;
            }
        }
        printf("%d ", matrix[i]);
    }
    return 0;
}
