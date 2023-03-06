#include <stdio.h>
/*
This code can do more than asked by the task.
You can provide a matrix size and it'll square it for you.
*/

//Calculates the dot product between two vectors (matrix rows)
int dotP(int A[], int B[], int n)
{
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        res = res + B[i] * A[i];
    }
    return res;
};


int main(void)
{
    int n = 0;
    printf("Enter matrix dimension:\n(n for n x n) ");
    scanf("%d", &n);
    int M2[n][n];
    int M1[n][n];

    for(int i=0; i<n; i++)
    {
        for(int j = 0; j<n; j++)
        {
            printf("\nEnter value\n(row %d, column %d): ", i+1, j+1);
            scanf("%d", &M1[i][j]);
        }
    }

    printf("\n");
    // Transposes accordingly (turns column to row)
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            M2[i][j] = M1[j][i];
        }
    }

    // Prints input matrix
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", M1[i][j]);
        }

        printf("        ");

        // Prints square matrix
        for (int j = 0; j < n; j++)
        {
            printf("%d ", dotP(M1[i], M2[j], n));
        }
        printf("\n");
     }
     printf("\n");
}