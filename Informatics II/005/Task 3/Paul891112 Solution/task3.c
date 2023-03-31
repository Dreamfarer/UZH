#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int higherHoarePartition(int A[], int l, int r){
    //Exact same Hoare Partition as in lecture

    int pivotj = A[r]; //pivot for j
    int j = r+1; int jj = l-1;

    while (1){
        j--;
        while(A[j]>pivotj){
            j--;
        }
        jj++;
        while(A[jj]<pivotj){
            jj++;
        }

        if(jj<j){
            //swap
            int temp = A[jj];
            A[jj] = A[j];
            A[j] = temp;
        }
        else{
            return jj;
        }
    }
}

int lowerHoarePartition(int A[], int l, int r){
    //Hoare partition using left most element as pivot, first increment i from left, decrement ii from right, in the end return ii which is equivalent to i in lecture

    int pivoti = A[l]; //pivot for i
    int i=l-1; int ii = r+1;

    while (1){
        i++;
        while(A[i]<pivoti){
            i++;
        }
        ii--;
        while(A[ii]>pivoti){
            ii--;
        }

        if(i<ii){
            //swap
            int temp = A[ii];
            A[ii] = A[i];
            A[i] = temp;

        }
        else{
            return ii;
        }
    }
}


void dpQuicksort(int A[], int l, int r){

    if(l>=r){
        return;
    }

    //assert left pivot < right pivot before sorting begins
    if (A[r] < A[l]){
        int t = A[r];
        A[r] = A[l];
        A[l] = t;
    }

    int n = higherHoarePartition(A,l,r);
    int m = lowerHoarePartition(A,l,r); 


    dpQuicksort(A,l,m);
    dpQuicksort(A,m+1,n-1);
    dpQuicksort(A,n,r);
}




int main(){

    //Konfigure array elements and size here, size = number of elements
    int A[] = {10,7,3,15,6,2,5,1,17,8,14,19,3,5,0};
    int size = 15;

    printf("Before: [ ");
    for (int i= 0;i < size; i++){
        printf("%d ", A[i]);
    }
    printf("]\n");

    dpQuicksort(A,0,size-1);

    printf("After: [ ");
    for (int i= 0;i < size; i++){
        printf("%d ", A[i]);
    }
    printf("]\n");
}