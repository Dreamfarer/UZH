#include <stdio.h>

void Rec(int A[], int n)
{
    if(n==0)
    {
        return;
    }

    int newA[n-1];
    for (int i = 0; i < n-1; i++)
    {
        newA[i] = A[i] + A[i + 1];
    }

    Rec(newA, n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    
    printf("\n");
}

int main(void)
{
    int A[] = {5,4,6,1,3};
    int n = sizeof(A) / sizeof(A[0]);
    Rec(A,n);
}