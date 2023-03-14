#include <stdio.h>
#include <time.h>

int linear_search(int A[], int n, int t) {
    for (int i = 0; i < n; i++) {
        if (A[i] == t) {
            return 1;
        }
    }
    return 0;
}

int binary_search(int A[], int n, int t) {
    int l = 0;
    int r = n - 1;
    int m;
    while (l <= r) {
        m = l + (r - l) / 2;
        if (A[m] == t) {
            return 1;
        }
        if (A[m] < t) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    return 0;
}

int main() {
    int n, t;

    printf("Enter an integer for n: ");
    scanf("%d", &n);
    printf("Enter an integer for t: \n");
    scanf("%d", &t);

    int A[n];

    printf("Generate an array with %d distinct integers from 1 to %d.\n", n, n);
    for (int i = 0; i < n; i++) {
        A[i] = i + 1;
    }

    clock_t start, end;

    start = clock();
    linear_search(A, n, t);
    end = clock();
    double run_time = ((double)(end - start)) / (CLOCKS_PER_SEC / 1000);
    printf("Linear search takes : %f millseconds\n", run_time);

    start = clock();
    binary_search(A, n, t);
    end = clock();
    run_time = ((double)(end - start)) / (CLOCKS_PER_SEC / 1000);
    printf("Binary search takes : %f millseconds\n", run_time);
}