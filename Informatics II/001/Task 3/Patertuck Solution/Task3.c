#include <stdio.h>

void pairSum(int Array[], int n, int c){
    int i, j;

    for (i=0; i<n-1; i++){
        for (j=i+1; j<n; j++){
            if(Array[i] + Array[j] == c){
                printf("Pair found: %d can be formed with %d and %d\n", c, Array[i], Array[j]);
                return;
            }
        }
    }
    printf("No pair found for %d\n", c);
}


// There are for sure more efficient ways to use the sorted Array
// If you wish to see that, check out @Codecycles Code on Github
void pairSumSorted(int Array[], int n, int c){
    int i, j;
    for (i=0; i<n-1; i++){
        for (j=0; j<n; j++){
            if(Array[i] + Array[j] == c){
                printf("Pair found: %d can be formed with %d and %d\n", c, Array[i], Array[j]);
            }
            if (Array[i] + Array[j] > c){
                n = j;
            }
        }
    }
    printf("No pair found for %d\n", c);

}


int main(){
    int Array[] = {5,3,2,1,2,4,5};
    int Array_sorted[] = {2,3,4,6,10,10,11,20};
    int n = sizeof(Array)/sizeof(Array[0]);
    int n_sorted = sizeof(Array_sorted)/sizeof(Array_sorted[0]);
    int c = 10;
    
    pairSum(Array, n, c);
    pairSumSorted(Array_sorted, n_sorted, c);

    return 0;
}