#include <stdio.h> // чтобы пользоваться функцией printf
#include <stdlib.h>
#include <time.h>

#define DATALENGTH 2000

int main() {
  int res = 0;
  int lenght = DATALENGTH;
  int b[DATALENGTH] = {0};
  int counts[DATALENGTH] = {0};
  int a[DATALENGTH] = {0};
  int i;
  srand(time(0));
  for (i = 0; i < DATALENGTH; i++) {
    a[i] = i + 1;
  }
  for (i = 0; i < DATALENGTH - 1; ++i) {
    int j = rand() % (DATALENGTH - i) + i;
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }
  for (i = 0; i < DATALENGTH; i++) {
    int x = a[DATALENGTH - 1 - i];
    int v = x - 1;
    while (v != 0) {
      res = res + counts[v - 1];
      v = v - (v & -v);
    }
    v = x;
    while (v <= lenght) {
      counts[v - 1] = counts[v - 1] + 1;
      v = v + (v & -v);
    }
  }
  printf("%d", res);

  return 0;
}
