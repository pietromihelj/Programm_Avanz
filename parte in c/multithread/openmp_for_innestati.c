#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  const int n = 20;
  int * M = (int *)malloc(n*n * sizeof(int));
   int * v = (int *)malloc(n * sizeof(int));
   for(int i= 0; i<n ; i++){
    v[i] = i*i;
   }
#pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++){
            M[i*n + j] = i*j;
            printf("ciclo i=%d j=%d è assegnato a %d\n", i, j, omp_get_thread_num());
        }
    }

int sum = 0;
#pragma omp parallel for reduction(+ : sum)
    for (int i = 0; i < n; i++) {
        sum += v[i];
    }
printf("somma:%d\n", sum);

int prod = 1;
#pragma omp parallel for reduction(* : prod)
    for (int i = 0; i < n; i++) {
        prod *= v[i] + 1;
    }
printf("prodotto:%d\n", prod);
  return 0;
}