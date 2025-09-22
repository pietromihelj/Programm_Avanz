#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  printf("a\n");
#pragma omp parallel
  {
    printf("b\n");
    printf("c\n");
  }
  printf("d\n");
 

#pragma omp parallel
{
  int x = 2;
  int y = rand()%10;
  x+=y;
  printf("aggiungo %d a x che ora vale %d\n", y,x);
}
 return 0;
}
