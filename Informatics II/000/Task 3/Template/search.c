/*

gcc search.c -o search; ./search  # Linux
gcc search.c -o search; ./search  # Windows (UCRT64)
gcc search.c -o search; ./search  # Mac

*/

#include <stdio.h>

#define n 5

int j, q;
int a[] = {11, 1, 4, -3, 22};

int main() {
  j = 0; q = -3;
  while (j < n && a[j] != q) { j++; }
  if (j < n) { printf("%d\n", j); }
  else { printf("NIL\n"); }
}
