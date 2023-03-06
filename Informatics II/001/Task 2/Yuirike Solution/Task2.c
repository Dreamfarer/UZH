#include <stdio.h>
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
    // Input version for 2x2 Case
    int n = 2;
    int M2[n][n];
    int M1[n][n];
    printf("Type a number: ");
    scanf("%d", &M1[0][0]);
    printf("Type a number: ");
    scanf("%d", &M1[0][1]);
    printf("Type a number: ");
    scanf("%d", &M1[1][0]);
    printf("Type a number: ");
    scanf("%d", &M1[1][1]);

    // Transposes accordingly
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            M2[i][j] = M1[j][i];
        }
    }

    // Print input matrix
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", M1[i][j]);
        }

        printf("  ");

        // Print square matrix
        for (int j = 0; j < n; j++)
        {
            printf("%d ", dotP(M1[i], M2[j], n));
        }
        printf("\n");
    }
}