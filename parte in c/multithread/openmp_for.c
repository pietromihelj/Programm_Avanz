#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int sum = 0;
#pragma omp parallel
{
  #pragma omp for
  for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
  
  }
  printf("finito ");
}
  return 0;
}
