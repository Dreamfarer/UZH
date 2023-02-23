#include <stdio.h>



int main() {
    int dimension_x = 2;
    int dimension_y = 2;
    int A[2][2];
    int A_quadrat[2 * 2];

    int A_temp[2*2];

    for (int i = 0; i < dimension_x * dimension_y; i++) {
        scanf("%d", &A_temp[i]);
    }

    A[0][0] = A_temp[0];
    A[0][1] = A_temp[1];
    A[1][0] = A_temp[2];
    A[1][1] = A_temp[3];

    int mulM[dimension_x][dimension_y];

    // Initializing all elements of result matrix to 0
    for (int i = 0; i<dimension_x; ++i) {
        for (int j = 0; j < dimension_y; ++j) {
            mulM[i][j] = 0;
        }
    }

    for (int i = 0; i<dimension_x; ++i) {
        for (int j = 0; j < dimension_y; ++j){
            for (int k = 0; k < dimension_x; ++k) {
                mulM[i][j] += A[i][k] * A[k][j];
            }
        }
    }
    printf("%d %d\t %d %d\n",A[0][0],A[0][1],mulM[0][0],mulM[0][1]);
    printf("%d %d\t %d %d\n",A[1][0],A[1][1],mulM[1][0],mulM[1][1]);

}



