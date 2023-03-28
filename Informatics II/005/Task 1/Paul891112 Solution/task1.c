#include <stdio.h>


void printHeap(int A[], int n, int d){
    //prints the created max-heap to the console in
//the format graph g f (all the edges in the form NodeA -- NodeB) g, where each edge should
//be printed in a separate line. The ordering of the edges is not relevant.

    if(n<2){return;} //heap with one or zero element has no children, dont print

    printf("g { \n");

    for(int i=0;i<=n/d;i++){
        for (int j=d*i+1;j<=(i+1)*d && j<n;j++){
            printf("\t%d -- %d \n", A[i],A[j]);
        }
    }
    printf("}\n\n");
}


void heapify(int A[], int i, int s, int d){
    //build heap structure of size s (not index) out of array A at node i, d = children of a node
    
    int child = 3*i+1; //index of first child
    int m=i; //placeholder for index of biggest elem
    for (int j=0;j<d;j++){ //go thru every child (j just to count)
        if (A[m]<A[child] && child<s){
            m=child; //remember the larger elem within heap range
        }
        child++; //increment child index
    }
    if (i != m){ //swap if a larger elem exists
        int temp = A[i];
        A[i] = A[m];
        A[m] = temp;
        heapify(A,m,s,d); //restore heap at the lower level node after swapping
    }
    printHeap(A,s,d);
}


void buildMaxHeap(int A[], int n, int d);
//A is the array to be converted, n
//is the real size of the array A and d is the maximum number of child each node can have in the
//heap.

void heapSort(int A[], int n, int d); //sorts in ascending order

void printArray(int A[], int n){//prints a given array to the console

    printf("Array: {");

    for(int i=0;i<n;i++){
        printf("%d, ", A[i]);
    }

    printf("}\n\n");

}


void buildMaxHeap(int A[], int n, int d){
    
    for (int i=(n-2)/d;i>=0;i--){ //c=(n-1) is the index of last child, (c-1)/d is the parent index of any c, so (n-2)/d is the largest parent index for heap of size n
        heapify(A,i,n,d);
    }
    printHeap(A,n,d);
}


void heapSort(int A[], int n, int d){
    
    //start with a maxheap
    buildMaxHeap(A,n,d);

    for (int i=n-1;i>=0;i--){
        
        int temp = A[i];
        A[i]=A[0];
        A[0]=temp;
        heapify(A,0,i,d);
        
    }  
}

int main(){
    //modify test input here

    //n=size of array, number of elements
    int n= 10;

    //A[] the actual array to be sorted
    int A[]={4,3,2,5,6,7,8,9,12,1};

    //d-ary heap, number of maximal children of each node
    int d = 3;


    //call heapSort and print the final result
    heapSort(A,n,d);
    printArray(A,n);
    

}

