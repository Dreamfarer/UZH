#include<stdio.h>
#include<stdlib.h>
#define N 5

void print(int *arr, int n){
    printf("%d", arr[0]);
    for(int i=1;i<n;i++){
        printf(", %d", arr[i]);
    }
    printf("\n");
}


int* reverse(int *arr, int n){

    int* p = malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        p[i] = arr[n-1-i];
    }
    return p;

}


int* prepend(int *arr, int v){
    int* p = arr-1;
    p[0] = v;
    return p;
}

int main(){

    int *arr;
    arr = malloc (N*sizeof(int));

    for(int i=0;i<N;i++){
        arr[i] = i;
    }

    printf("The original: ");
    print(arr, N);

    int *reversed = reverse(arr, N);

    free(arr);

    printf("The reversed: ");
    print(reversed, N);

    int *prepended = prepend(reversed, 5);

    free(reversed);

    printf("The prepended: ");
    print(prepended, N+1);

}

