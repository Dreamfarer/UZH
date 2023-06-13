#include <stdio.h>
#include <limits.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

int isPalindrome(char s[], int l, int r) {
    while (r > l) {
        if (s[l++] != s[r--]) {
            return 0;
        }
    }
    return 1;
}

int findMinCutsRecursive(char s[], int l, int r) {
    if (l == r || isPalindrome(s, l, r)) {
        return 0;
    }
    int result = INT_MAX;
    for (int i = l; i < r; i++) {
        int v = 1 + findMinCutsRecursive(s, l, i) + findMinCutsRecursive(s, i + 1, r);
        if (v < result) {
            result = v;
        }
    }
    return result;
}

int findMinCuts(char s[], int length) {
    int m[length][length];
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            m[i][j] = 0;
        }
    }
    for (int i = length - 1; i >= 0; i--) {
        for (int j = i; j < length; j++) {
            if (i == j) {
                m[i][j] = 1;
                continue;
            }
            if (s[i] == s[j]) {
                if (j - i == 1) {
                    m[i][j] = 1;
                } else {
                    m[i][j] = m[i + 1][j - 1];
                }
                continue;
            }
            m[i][j] = 0;
        }
    }
    int h[length];
    for (int i = 0; i < length; i++) {
        h[i] = INT_MAX;
    }
    for (int i = length - 1; i >= 0; i--) {
        if (m[i][length - 1] == 1) {
            h[i] = 0;
            continue;
        }
        for (int j = length - 2; j > i - 1; j--) {
            if (m[i][j] == 1) {
                h[i] = min(h[i], 1 + h[j + 1]);
            }
        }
    }
    return h[0];
}

int main() {
    char s[] = "ABBCDC";
    printf("%d\n", findMinCuts(s, 6));
    return 0;
}