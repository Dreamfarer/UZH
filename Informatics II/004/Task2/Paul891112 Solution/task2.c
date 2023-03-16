#include <stdio.h>
#include<math.h>
int counter;
int algo(int count, int c1){

    if (count == 1){
        counter++;
        return 1;
    }
    counter++;
    return 2*algo(count-1, c1) + c1; 

}

int main(){
    
    int c1 = 2;
    for (int i=1;i<=10;i++){
        printf("%d, guess: %d\n",algo(i,c1),(int)pow((double)2,i-1)*(1+c1)-c1);
    }
    
}