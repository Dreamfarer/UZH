#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int longestPath(int width, int height, int m[height][width]) {
    int s[height][width];
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            s[y][x] = INT_MIN;
        }
    }
    int longest = 0;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int left = abs(m[y][x] - m[y][x - 1]);
            int up = abs(m[y][x] - m[y - 1][x]);
            if (x - 1 >= 0 && y - 1 >= 0 && left && up <= 1) {
                s[y][x] = max(1, max(s[y][x - 1] + 1, s[y - 1][x] + 1));
            } else if (x - 1 >= 0 && left <= 1) {
                s[y][x] = max(1, s[y][x - 1] + 1);
            } else if (y - 1 >= 0 && up <= 1) {
                s[y][x] = max(1, s[y - 1][x] + 1);
            } else {
                s[y][x] = 1;
                continue;
            }
            if (s[y][x] > longest) {
                longest = s[y][x];
            }
        }
    }
    return longest;
}

int main(){
    int m[5][4] = {
        {4, 6, 7, 8},
        {3, 2, 3, 8},
        {8, 6, 6, 7},
        {9, 5, 2, 5},
        {8, 4, 3, 2}
    };
    printf("%d\n", longestPath(4, 5, m));
    return 0;
}