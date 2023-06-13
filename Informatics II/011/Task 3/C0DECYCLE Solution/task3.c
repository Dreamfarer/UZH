#include <stdio.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

void makeHelper(int width, int height, int m[height][width], int top[height][width], int bottom[height][width], int left[height][width], int right[height][width]) {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (m[i][j] == 1) {
                if (i - 1 >= 0) {
                    top[i][j] = top[i - 1][j] + 1;
                } else {
                    top[i][j] = 1;
                }
                if (j - 1 >= 0) {
                    left[i][j] = left[i][j - 1] + 1;
                } else {
                    left[i][j] = 1;
                }
                continue;
            }
            top[i][j] = 0;
            left[i][j] = 0;
        }
    }
    for (int i = height - 1; i >= 0; i--) {
        for (int j = width - 1; j >= 0; j--) {
            if (m[i][j] == 1) {
                if (i + 1 < height) {
                    bottom[i][j] = bottom[i + 1][j] + 1;
                } else {
                    bottom[i][j] = 1;
                }
                if (j + 1 < width) {
                    right[i][j] = right[i][j + 1] + 1;
                } else {
                    right[i][j] = 1;
                }
                continue;
            }
            bottom[i][j] = 0;
            right[i][j] = 0;
        }
    }
}

int biggest_plus(int width, int height, int m[height][width]) {
    int bottom[height][width];
    int top[height][width];
    int left[height][width];
    int right[height][width];
    makeHelper(width, height, m, top, bottom, left, right);
    int biggest = 0;
    int s[height][width];
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            s[i][j] = min(bottom[i][j], min(top[i][j], min(left[i][j], right[i][j])));
            if (s[i][j] < 1) {
                s[i][j] = 0;
            } else {
                s[i][j] = (s[i][j] - 1) * 4 + 1;
            }
            if (s[i][j] > biggest) {
                biggest = s[i][j];
            }
        }
    }
    return biggest;
}

int main() {
    int m[5][6] = {
        {0, 0, 0, 1, 0, 0},
        {0, 1, 0, 1, 0, 0},
        {1, 1, 1, 1, 1, 1},
        {1, 1, 0, 1, 0, 1},
        {1, 0, 0, 1, 1, 0}
    };
    printf("%d\n", biggest_plus(6, 5, m));
    return 0;
}