#include <stdio.h>

void swap(int *a,int i, int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

//diffrent type of partition algorithm 
int lomuto_partition(int *a, int s, int e){
    int index_pivot = s;
    int pivot = a[e];
    for(int i = s; i < e; i++){
        if(a[i] < pivot){
            swap(a,index_pivot,i);
            index_pivot++;
        }
    }
    swap(a,index_pivot,e);
    return index_pivot;
}

//relevant partition algorithm for the lecture
int hoare_partition(int *a, int s, int e){
    int pivot = a[e];
    int i = s;
    int j = e;
    while(i <j){
        while(pivot<a[j]) j--;
        while(pivot>a[i]) i++;
        swap(a,j,i);
    }
    return i;
}

void quick_sort(int *a,int s, int e){
    int index;
    if (s >= e){
        return;
    }
    index = hoare_partition(a, s, e);
    quick_sort(a, s, index - 1);
    quick_sort(a,index + 1, e);

    }

int main(){
    int n = 10;
    int arr[10] = {6,3,30,22,12,5,14,9,7,4};
    int start = 0;
    int end = n;
    quick_sort(arr, start, end);

    for(int i=0;i<end;i++){
        printf("%d ", arr[i]);
    }
    return 0;
    }
    
