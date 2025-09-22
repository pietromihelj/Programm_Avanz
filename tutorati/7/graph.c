#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>
#include "graph.h"


void shortcut_std(float * m, float * d, int n)
{ int min_val;
  for(int i = 0; i<n ; i++){
    for(int j = 0; j<n; j++){
      min_val = INFINITY;
      for(int k = 0; k<n; k++){
        if (d[i*n+k] + d[k*n+j] < min_val){
          min_val = d[i*n+k]+d[k*n+j];
        } 
      }
      m[i*n+j] = min_val;
    }
  }
}

void shortcut_trs(float * m, float * d, int n)
{
  float * t = (float *) malloc(n * n * sizeof(float));
  #pragma omp parallel for collapse(2)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      t[j * n + i] = d[i * n + j];
    }
  }
  int min_val;
  for(int i = 0; i<n ; i++){
    for(int j = 0; j<n; j++){
      min_val = INFINITY;
      for(int k = 0; k<n; k++){
        if (d[i*n+k] + t[j*n+k] < min_val){
          min_val = d[i*n+k]+t[j*n+k];
        } 
      }
      m[i*n+j] = min_val;
    }
  }
  free(t);
}

void shortcut_omp(float * m, float * d, int n)
{
  #pragma omp parallel for collapse(2)
  for(int i = 0; i<n ; i++){
    for(int j = 0; j<n; j++){
      int min_val = INFINITY;
      for(int k = 0; k<n; k++){
        if (d[i*n+k] + d[k*n+j] < min_val){
          min_val = d[i*n+k]+d[k*n+j];
        } 
      }
      m[i*n+j] = min_val;
    }
  }
}

void shortcut(float * m, float * d, int n)
{
  float * t = (float *) malloc(n * n * sizeof(float));
  #pragma omp parallel 
  {
  #pragma omp for collapse(2)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      t[j * n + i] = d[i * n + j];
    }
  }
  #pragma omp for collapse(2)
  for(int i = 0; i<n ; i++){
    for(int j = 0; j<n; j++){
      int min_val = INFINITY;
      for(int k = 0; k<n; k++){
        if (d[i*n+k] + t[j*n+k] < min_val){
          min_val = d[i*n+k]+t[j*n+k];
        } 
      }
      m[i*n+j] = min_val;
    }
  }
  }
  free(t);
}
