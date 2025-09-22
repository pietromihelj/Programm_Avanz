#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include "netpbm.h"

int open_image(char * path, netpbm_ptr img)
{
  img->fd = fopen(path, "r+");
  if (img->fd == NULL) {
    return -1;
  }

  struct stat sbuff;
  stat(path, &sbuff);
  img->size = sbuff.st_size;

  if(fscanf(img->fd, "P5\n%d %d\n255\n", &img->width, &img->height)!=2){
    fclose(img->fd);
    return -2;
  }

  img->offset = ftell(img->fd);
  img->data = (char*) mmap((void*)0, img->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno(img->fd), 0);
  if(img->data == MAP_FAILED)
  {
    fclose(img->fd);
    return -3;
  }
  return 0;
}

int empty_image(char * path, netpbm_ptr img, int width, int height)
{
  FILE * fd = fopen(path, "w+");
  if (fd == NULL) {
    return -1;
  }
  int written = fprintf(fd, "P5\n%d %d\n255\n", width, height);
  ftruncate(fileno(fd), written + width * height);
  fclose(fd);
  return open_image(path, img);
}

char * pixel_at(netpbm_ptr img, int x, int y)
{
  if(img == NULL || x>=img->width || y >= img->height || x<0 || y<0){
  return NULL;
  }
  return img->data + (y*img->width + x);
}

int close_image(netpbm_ptr img)
{
  if(img == NULL){
  return -1;
  }
  munmap(img->data, img->size);
  fclose(img->fd);
  return 0;
}