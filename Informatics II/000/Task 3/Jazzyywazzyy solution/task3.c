#include <stdio.h>

int main(){
    int max_num, second_max; 
    int nums[] = {7,4,3,2,8}; 
    int array_len = sizeof(nums)/sizeof(nums[0]);

    if (nums[0] > nums[1]){
        max_num = nums[0]; 
        second_max = nums[1];
    }else{
        max_num = nums[1]; 
        second_max = nums[0]; 
    }

    for(int i = 2; i < array_len; i++){
        if (max_num < nums[i]){
            second_max = max_num; 
            max_num = nums[i]; 
        }else if(second_max < nums[i]){
            second_max = nums[i]; 
        }
    }
    printf("Second largest number: %d", second_max); 
    }
    

 