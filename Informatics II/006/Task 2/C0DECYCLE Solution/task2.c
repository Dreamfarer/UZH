#include<stdio.h>
#include<stdlib.h>

#define N 5

void print(const int* arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));
    }
}

int* reverse(const int* arr, int n) {
    int* reversed = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        *(reversed + i) = *(arr + n - (i + 1));
    }
    return reversed;
}

int* prepend(const int* arr, int n, int v) {
    int* prepended = malloc((n + 1) * sizeof(int));
    *(prepended) = v;
    for (int i = 0; i < n; i++) {
        *(prepended + (i + 1)) = *(arr + i);
    }
    return prepended;
}

int main() {
    int* arr = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        *(arr + i) = i;
    }
    printf("The original: ");
    print(arr, N);

    int *reversed = reverse(arr, N);
    free(arr);
    printf("\nThe reversed: ");
    print(reversed, N);

    int *prepended = prepend(reversed, N, 5);
    free(reversed);
    printf("\nThe prepended: ");
    print(prepended, N + 1);
}