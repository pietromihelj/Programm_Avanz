#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int sum = 0;
#pragma omp parallel
  {
    int local_sum = 0;
    for(int i = 0; i < 1000; i++){
    int n_thread = omp_get_thread_num();
    local_sum += n_thread + i;
#pragma omp critical
    {
      sum += local_sum;
    }
  }
  }
  printf("La somma dei valori è %d\n", sum);
  return 0;
}
