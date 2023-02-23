#include <stdio.h>

int main() {
	int n = 5;
	int A[] =  { 11, 3, -3, 2, -5};
	
	int pos1 = 0;
	int temp1 = A[pos1];
	for(int i = 0; i < n; i++ ) {
		if(A[i] > temp1) {
			pos1 = i;
			temp1 = A[i];
		}
	}

	int pos2;
	if(pos1 == 0) {
		pos2 = 1;
	} else{
		pos2 = 0;
	}
	int temp2 = A[pos2];
	for(int i = 0; i < n; i++ ) {
		if(i != pos1 && A[i] > temp2) {
			pos2 = i;
			temp2 = A[i];
		}
	}
	printf("%d\n", A[pos2]);
}