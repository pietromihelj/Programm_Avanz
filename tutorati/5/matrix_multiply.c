#include "matrix_multiply.h"

void simple_multiply(float* A, float* B, float* C, int n)
{
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        C[i * n + j] += A[i * n + k] * B[k * n + j];
      }
    }
  }
}

void transposed_multiply(float * A, float * B, float * C, int n)
{
  for (int j = 0; j < n; j++){
     for (int i = 0; i < n; i++){
      for (int k = 0; k < n; k++) {
        C[i * n + j] += A[i * n + k] * B[j * n + k];
      }
    }
  }
}

void kernel(float* A, float* B, float* C, int x, int dx, int y, int dy, int z, int dz, int n)
{
 int c = n < x+dx;
 int c1= n < y+dy;
 int c2= n < z+dz;
 c = c*n+(1-c)*(x+dx);
 c1 = c1*n+(1-c1)*(y+dy);
 c2 = c2*n+(1-c2)*(z+dz);
 for (int j = y; j < c1; j++){
     for (int i = x; i < c; i++){
      for (int k = z; k < c2; k++) {
        C[i * n + j] += A[i * n + k] * B[j * n + k];
      }
    }
  }
}

int s = 16; // Dimensione dei blocchi, provare inizialmente con 2 o 4

void blocked_multiply(float* A, float* B, float* C, int n)
{
  const int s1 = s;
  const int s2 = s;
  const int s3 = s;
  for(int x = 0; x < n; x+=s1){
    for(int y = 0; y < n; y+=s2){
      for(int z = 0; z < n; z+=s3){
        kernel(A,B,C,x,s1,y,s2,z,s3,n);
      }
    }
  }
}