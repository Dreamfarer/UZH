#include<stdio.h>
#include<stdlib.h>
#define N 5

// A
void print(int *arr, int n){
    printf("[");

    for (int i = 0; i < n; i++){
        printf("%d", *(arr + i));

        if (i < n - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

// B
int* reverse(int *arr, int n){
    int* temp = malloc(N * sizeof(int));

    for (int i = 0; i < n; i++){
        *(temp + i) = *(arr + n - 1 - i); 
    }

    return temp;  
}

// C
int* prepend(int *arr, int v, int n){
    int* temp = malloc((n + 1) * sizeof(int));
    *temp = v;

    for (int i = 0; i < n; i++){
        *(temp + i + 1) = *(arr + i);
    }

    return temp;
}

int main() {
    int *arr;
    arr = malloc((N + 1) * sizeof(int));

    for (int i = 0; i < N; i++) {
        arr[i] = i;
    }


    printf("The original: ");
    print(arr, N);
    int *reversed = reverse(arr, N);

    free(arr);

    printf("The reversed: ");
    print(reversed, N);

    int *prepended = prepend(reversed, 5, N);

    free(reversed);

    printf("The prepended: ");
    print(prepended, N + 1);
}
