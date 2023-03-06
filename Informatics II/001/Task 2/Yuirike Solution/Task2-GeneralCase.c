#include <stdio.h>
/*
Test this code for general n x n cases
If you use VSCode, you can run this with Code-Runner.
*/

//Function to calculate the dot product
int dotP(int A[], int B[], int n)
{
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                res = res + B[j] * A[i];
            }
        }
    }
    return res;
};


//Example case with a 4x4 matrix
int main(void)
{
    int A[4][4] = {{1, 2, 4, 6}, {3, 4, 2, 6}, {1, 2, 4, 6}, {1, 2, 4, 6}};
    int B[4][4];
    int n = 4;

    // Transpose accordingly
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            B[i][j] = A[j][i];
        }
    }

    // Print input matrix
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", A[i][j]);
        }

        printf("  ");

        // Print square matrix
        for (int j = 0; j < n; j++)
        {
            printf("%d ", dotP(A[i], B[j], n));
        }
        printf("\n");
    }
}