#include <stdio.h>

#define DISKS 4
#define MOVE 15

int m = MOVE;
int s[3][DISKS];

void printHanoi() {
    for (int c = 0; c < DISKS; c++) {
        for (int p = 0; p < 3; p++) {
            if (s[p][c] > -1) {
                printf(" %d", s[p][c]);
            } else {
                printf(" |");
            }
        }
        printf("\n");
    }
}

void move(int d, int from, int to) {
    if (m > 0) {
        m -= 1;
        int i = d - 1;
        s[from][i] = -1;
        s[to][i] = i;
        //printf("\n> Disk %d from peg %d to peg %d (Move #%d)\n", i, from, to, MOVE - m);
        //printHanoi();
    }
}

void hanoi(int d, int from, int inter, int to) {
    if (d == 1) {
        move(d, from, to);
        return;
    }
    hanoi(d - 1, from, to, inter);
    move(d, from, to);
    hanoi(d - 1, inter, from, to);
}

void init() {
    for (int p = 0; p < 3; p++) {
        for (int c = 0; c < DISKS; c++) {
            s[p][c] = -1;
            if (p == 0) {
                s[p][c] = c;
            }
        }
    }
}

int main(){
    init();
    //printHanoi();
    hanoi(DISKS, 0, 1, 2);
    printHanoi();
    return 0;
}