#include <stdio.h>

void pairSum(int n, int A[], int c) {
    int i, j;

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (A[i] + A[j] == c) {
                printf("Found pair sum!\n");
                return;
            }
        }
    }

    printf("No pair sum!\n");
}

void pairSum_sorted(int n, int A[], int c) {
    int l = 0;
    int u = n - 1;

    while (l < u) {
        if (A[l] + A[u] == c) {
            printf("Found pair sum!\n");
            return;
        }

        if (A[l] + A[u] < c) {
            l++;
        } else {
            u--;
        }
    }

    printf("No pair sum!\n");
}

int main() {
    int n = 7;
    int A[] = {18, 33, 12, 45, 26, 3, 2};
    int A_sorted[] = {2, 3, 18, 21, 26, 33, 45};
    int c = 44;

    pairSum(n, A, c);
    pairSum_sorted(n, A_sorted, c);

    return 0;
}