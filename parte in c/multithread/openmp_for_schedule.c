#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int sum = 0;
#pragma omp parallel
  {
#pragma omp for schedule(static, 2)
    for (int i = 0; i < 10; i++) {
      printf("%d\n", omp_get_thread_num());
    }
    
    }
  return 0;
}