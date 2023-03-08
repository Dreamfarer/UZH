#include <stdio.h>
/*
I solved it before but had to get some help to figure out how to turn it.
If anyone is good enough at code analysis, could you explain:

Why n-1 seems to be such a crucial thing? I understand why it has to be in the recursive function but why also in the loop?

Why does this work, i.e., why do I have to put the recursive call between for-loops?

I tried to pull off this code with only the original array but that didn't work, is it because the original array 
would contain other values? 
*/

void Rec(int A[], int n)
{
    if(n!=0)
    {
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
    }
            printf("\n");
    }

int main(void)
{
    int A[] = {5,4,6,1,3};
    int n = sizeof(A) / sizeof(A[0]);
    Rec(A,n);


}