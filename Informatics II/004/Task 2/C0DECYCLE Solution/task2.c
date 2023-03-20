#include <stdio.h>

int ta(int n, int c1) {
    int r = 1;
    if (n != 1) {
        r = 2 * ta(n - 1, c1) + c1;
    }
    printf("%d\n", r);
    return r;
}

int main() {
    ta(5, 6);
}