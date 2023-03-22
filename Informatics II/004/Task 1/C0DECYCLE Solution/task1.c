#include <stdio.h>
#include <limits.h>

int max(int x, int y) {
    if (x > y) {
        return x;
    }
    return y;
}

int maxCombineSum(int A[], int l, int m, int r) {
    int s = 0;
    int leftS = INT_MIN;
    for (int i = m; l - 1 < i; i--) {
        s += A[i];
        leftS = max(s, leftS);
    }
    s = 0;
    int rightS = INT_MIN;
    for (int i = m; i < r + 1; i++) {
        s += A[i];
        rightS = max(s, rightS);
    }
    return max(max(leftS, rightS), leftS + rightS - A[m]);
}

int maxSubSum(int A[], int l, int r) {
    if (l > r) {
        return INT_MIN;
    }
    if (l == r) {
        return A[r];
    }
    int m = (l + r) / 2;
    return max(
        max(maxSubSum(A, l, m - 1), maxSubSum(A, m + 1, r)),
        maxCombineSum(A, l, m, r)
    );
}

int main() {
    int n = 7;
    int A[] = {-2, -5, 6, -2, -3, 1, 5};
    printf("%d", maxSubSum(A, 0, n - 1));
}