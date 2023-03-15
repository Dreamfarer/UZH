#include <stdio.h>
#include <time.h> // measuring run time

int n, t;
int A[100000000];

int linear_search(int A[], int n, int t) {
    for (int i = 0; i < n; i++) {
        if (A[i] == t) {
            return i;
        }
    }
    return -1;
}

int binary_search(int A[], int l, int r, int t) {
    /* Binary search adjust its boundaries until there is only one element left
    (Divide & Conquer). If the searched element is not in the array, it will
    cross-over the boundaries (because we add/subtract 1 to the middle) and
    the following condition turns true.*/
    if (l > r) {
        return -1;
    }
    else {
        int m = (l + r) / 2;
        if (A[m] == t) {
            return m;
        }
        else if (t < A[m]) {
            // Adjust boundaries to [left, middle - 1]
            return binary_search(A, l, m - 1, t);
        }
        else {
            // Adjust boundaries to [middle + 1, right]
            return binary_search(A, m + 1, r, t);
        }
    }
}

int main() {
    clock_t start, end;

    printf("Enter an integer for n: ");
    scanf("%d", &n);
    printf("Generate an array with %d distinct integers from 1 to %d.\n", n, n);

    for (int i = 0; i < n; i++) A[i] = i + 1;
    printf("Enter an integer for t: \n");
    scanf("%d", &t);

    start = clock();
    linear_search(A, n, t);
    end = clock();

    double run_time = ((double)(end - start)) / (CLOCKS_PER_SEC / 1000);
    printf("Linear search takes : %f millseconds\n", run_time);

    start = clock();
    binary_search(A, 0, n - 1, t);
    end = clock();
    run_time = ((double)(end - start)) / (CLOCKS_PER_SEC / 1000);
    printf("Binary search takes : %f millseconds\n", run_time);
}