#include <stdio.h>
#include <math.h>
#define N 13

int arr[N] = {0,2,7,8,3,9,4,1,6,11,14,12,17};

//function to swap 2 elements
void swap(int *a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
}
//determine the index of right child 
int right(int i){
    return i*2+2;
}

//determine the index of left child 
int left(int i){
    return i*2+1;
}

//convert the tree to a heap from the index i downwards
void heapify(int *A, int i , int k){
    int m, l, r;
    m = i;
    l = left(i);
    r = right(i);

    //compare parent to children and remeber index if parent is smaller
    if (l<k && A[l] > A[m]){
        m = l;
    }
    if (r<k && A[r] > A[m]){
        m = r;
    }
    
    //swap bigger child with parent and call heapify with the new child as start index
    if(i!=m){
        swap(A, i, m);
        heapify(A, m, k);
    }
}

//iterate through all parent nodes and heapify 
void Build_heap(int *A,int l){
    for (int i = (l/2)-1; i>=0; i--){
        heapify(A,i,l);
    }
}

void Heap_sort(int *A, int p){
    int s = p;
    //convert to a heap
    Build_heap(A, p);
    //biggest element must be at the top therefore you can swap it to the end and call heapify
    //on the list that is one element shorter then before so the bigest element in the back
    //doesn't get touched
    for (int i = 0; i < p; i++){
        swap(A, 0, p-1-i);
        s--;
        heapify(A,0,s);
    //now 2. biggest element is at the top
    }
}


int main(){

    Heap_sort(arr, N);

    for (int i=0; i<N; i++){
        printf("%d ", arr[i]);
    }

    return 0;

}
