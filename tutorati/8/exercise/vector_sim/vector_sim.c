#include <math.h>
#include <omp.h>
#include <stdlib.h>
#include "vector_sim.h"

float cos_sim(float * v1, float * v2, int len)
{ float somma = 0;
  float len_v1 = 0;
  float len_v2 = 0;
  for( int i = 0; i < len; i++){
      somma += v1[i] * v2[i];
      len_v1 += v1[i]*v1[i];
      len_v2 += v2[i]*v2[i];
  }
  return (somma / (sqrtf(len_v1) * sqrtf(len_v2)));
}

int most_similar(float * v, float * M, int nrows, int ncols)
{
  float max_sim = -INFINITY;
  int max_sim_index = 0;
  for(int i = 0; i < nrows*ncols; i+=ncols){
    float sim = cos_sim(v,M+i,ncols);
    if(max_sim < sim){
      max_sim = sim;
      max_sim_index = i;
    }
  }

  return(max_sim_index/ncols);
}

int omp_most_similar(float * v, float * M, int nrows, int ncols)
{
  float max_sim = -INFINITY;
  int max_index = 0;
  
  #pragma omp parallel
  {
  float loc_max_sim = -INFINITY;
  int loc_max_index = 0;
  #pragma omp for nowait
  for(int i = 0; i < nrows*ncols; i+=ncols){
    float sim = cos_sim(v,M+i,ncols);
    if(loc_max_sim < sim){
      loc_max_sim = sim;
      loc_max_index = i;
    }
  }
  #pragma omp critical
  {
    if(max_sim < loc_max_sim){
      max_sim = loc_max_sim;
      max_index = loc_max_index;
    }
  }

  }

  return (max_index/ncols);
}