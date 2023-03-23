#include <stdio.h>
#include <math.h>
#define N 13

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
void heapify(int *a, int i , int k){
    int m, l, r;
    m = i;
    l = left(i);
    r = right(i);

    //compare parent to children and remeber index if parent is smaller
    if (l<k && a[l] > a[m]){
        m = l;
    }
    if (r<k && a[r] > a[m]){
        m = r;
    }
    
    //swap bigger child with parent and call heapify with the new child as start index
    if(i!=m){
        swap(a, i, m);
        heapify(a, m, k);
    }
}

//iterate through all parent nodes and heapify 
void Build_heap(int *a,int k){
    for (int i = (k/2)-1; i>=0; i--){
        heapify(a,i,k);
    }
}

void Heap_sort(int *a, int k){
    int s = k;
    //convert to a heap
    Build_heap(a, k);
    //biggest element must be at the top therefore you can swap it to the end and call heapify
    //on the list that is one element shorter than before so the biggest element in the back
    //doesn't get touched
    for (int i = 0; i < k; i++){
        swap(a, 0, k-1-i);
        s--;
        heapify(a,0,s);
    //now 2. biggest element is at the top
    }
}


int main(){

    int arr[N] = {0,2,7,8,3,9,4,1,6,11,14,12,17};

    Heap_sort(arr, N);

    for (int i=0; i<N; i++){
        printf("%d ", arr[i]);
    }

    return 0;

}
