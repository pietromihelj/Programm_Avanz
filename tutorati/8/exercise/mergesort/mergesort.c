#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <omp.h>

int * random_vector(int len)
{
  int * v = (int*) malloc(len * sizeof(int));
  for (int i = 0; i < len; i++) {
    v[i] = rand();
  }
  return v;
}

void merge(int * v1, int n1, int * v2, int n2, int * results)
{
  int i = 0, j = 0, k = 0;
  while ((i < n1) && (j < n2)) {
    if (v1[i] < v2[j]) {
      results[k] = v1[i];
      i++;
    } else {
      results[k] = v2[j];
      j++;
    }
    k++;
  }
  memcpy(results+k, v1+i, sizeof(int) * (n1-i));
  memcpy(results+k, v2+j, sizeof(int) * (n2-j));
}

void merge_sort(int * v, int len)
{
  int * origin = v;
  int * u = (int*) malloc(len * sizeof(int));
  for (int i = 1; i < len; i *= 2) {
    for (int j = 0; j < len; j += 2*i) {
      if (j+i < len) {
        int k = (j+2*i <= len) ? i : (len-j-i);
        merge(v+j, i, v+(j+i), k, u+j);
      } else {
        memcpy(u+j, v+j, (len-j) * sizeof(int));
      }
    }
    int * tmp = v;
    v = u;
    u = tmp;
  }
  if (v == origin) {
    free(u);
  } else {
    memcpy(origin, v, len * sizeof(int));
    free(v);
  }
}

void merge_sort_parallel(int * v, int len)
{
  int * origin = v;
  int * u = (int*) malloc(len * sizeof(int));
   
  for (int i = 1; i < len; i += i) {
    #pragma omp parallel for
    for (int j = 0; j < len; j += 2*i) {
      if (j+i < len) {
        int k = (j+2*i <= len) ? i : (len-j-i);
        merge(v+j, i, v+(j+i), k, u+j);
      } else {
        memcpy(u+j, v+j, (len-j) * sizeof(int));
      }
    }
    int * tmp = v;
    v = u;
    u = tmp;
  }
  if (v == origin) {
    free(u);
  } else {
    memcpy(origin, v, len * sizeof(int));
    free(v);
  }
}

double test_mergesort(int n, void (* m) (int *, int))
{
  int * v = random_vector(n);
  double start = omp_get_wtime();
  m(v, n);
  double end = omp_get_wtime();
  double ms = (end - start) * 1000;
  free(v);
  return ms;
}

int main(int argc, char * argv[])
{
  srand(time(NULL));
  const int n = 1 << 20;
  printf("Sequential\tParallel\n");
  double t1, t2;
  t1 = test_mergesort(n, merge_sort);
  t2 = test_mergesort(n, merge_sort_parallel);
  printf("%f\t%f\n", t1, t2);
  return 0;
}