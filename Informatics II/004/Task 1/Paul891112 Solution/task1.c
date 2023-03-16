#include <stdio.h>



void combine(int A[], int l, int r, int m, int* left, int* right){
    //pre: index of left most elem, r = index of right most index, m=(l+r)/2, pointers to global left,right index
    //post: updates pointers to the left and right index of the largest sum subarray (lss)
    
    int lsum =0; int rsum=0; int sum=0;
    
    
    for (int i=*left;i<=m;i++){
        lsum += A[i];
        sum += A[i];
    }
    for (int i=m+1;i<=*right;i++){
        sum += A[i];
        rsum += A[i];
    }
    
    if (lsum > sum && lsum > rsum){ //left subarray has largest sum
        if(r>=*right){
            *right=m; 
            //only update right lss index if we take the left sum and 
            //we are omitting the right bound of original array
        }
        //*right = m;


        /*printf("Largest subarray: [");
    for (int i=*left;i<=*right;i++){
        printf("%d, ",A[i]);
    }
    printf("]\n");*/
        
    }
    else if(rsum > sum){//right subarray has largest sum
        if (l<=*left){
            *left = m+1;
            //only update left index when we take the right sum
            //and the current left bound we are throwing away
            //is less or equal to (to the left of) the current lls left index.
            
            
        }
        
        /*
        printf("Largest subarray: [");
    for (int i=*left;i<=*right;i++){
        printf("%d, ",A[i]);
    }
    printf("]\n");*/

        
    }
    else{
        //if we take the full sum, do nothing
        /*
        printf("Largest subarray: [");
    for (int i=*left;i<=*right;i++){
        printf("%d, ",A[i]);
    }
    printf("]\n");*/
    

    }

    //printf("*left: %d, *right: %d\n\n", *left, *right);

    return;
}

void maxsubarray(int A[],int l, int r, int* left, int* right){
    int m=(r+l)/2;
    if (l==r){
        return;
    }
    
    maxsubarray(A,l,m, left, right);
    maxsubarray(A,m+1,r, left, right);
    combine(A,l,r,m, left, right);

    
    return;
}



int main(){

    //Change the input array here
    int A[]={-2,-5,6,-2,-3,1,5};

    //initialize pointers to first and last index of original array
    int left=0; 
    int right=6;

    //pass the address of the pointers to lss indices
    maxsubarray(A,0,6,&left, &right);
    printf("Largest subarray: [");
    for (int i=left;i<=right;i++){
        if(i==left){
            printf("%d",A[i]);
            continue;
        }
        printf(", %d",A[i]);
    }
    printf("]\n");


}