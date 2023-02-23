#include <stdio.h>
#include <limits.h>

int main() {

    int pos_largest, pos_second;
    int largest_number = INT_MIN;
    int second_largest_number = INT_MIN;
    int A[] = {4, 3, 11, 133, 9, 8, 312};
    int len_array = sizeof(A)/sizeof(A[0]);

    for (int i = 0; i < len_array; i++ ) {
    
        if (A[i] > largest_number){
            second_largest_number = largest_number;
            largest_number = A[i];
            pos_second = pos_largest;
            pos_largest = i;
        
        }

        else if(A[i] > second_largest_number) {
            second_largest_number = A[i];
            pos_second = i;
        }
    }

    printf("Second Largest Number is %d at position %d\n", second_largest_number, pos_second + 1);
    return 0;
}