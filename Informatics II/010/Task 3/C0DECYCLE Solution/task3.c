#include <stdio.h>

void init(int A[], int n) {
    for (int i = 0; i < n; i++) {
        A[i] = 0;
    }
}

int hash(int k, int i, int n) {
    int hash1 = (k % n) + 1;
    int hash2 = (n - 1) - (k % (n - 1));
    return (hash1 + i * hash2) % n;
}

int insert(int A[], int n, int key) {
    int counter = 0;
    int i;
    do {
        i = hash(key, counter, n);
    } while(A[i] != 0 && counter++ < n);
    A[i] = key;
    return i;
}

int search(int A[], int n, int key) {
    int counter = 0;
    int i;
    do {
        i = hash(key, counter, n);
    } while(A[i] != key && A[i] != 0 && counter++ < n);
    return (A[i] == key) ? i : -1;
}

void print(int A[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d: %d\n", i, A[i]);
    }
}

int main() {
    int n = 7;
    int A[n];
    init(A, n);
    insert(A, n, 12);
    insert(A, n, 5);
    insert(A, n, 8);
    insert(A, n, 31);
    insert(A, n, 1);
    insert(A, n, 2);
    insert(A, n, 3);
    print(A, n);
    printf("%d\n", search(A, n, 31));
    return 0;
}