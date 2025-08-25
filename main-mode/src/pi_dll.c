/* filename: pi_dll.c - DLL version */
#define BUILDING_PI_DLL
#include "pi_dll.h"
#include <stdlib.h>
#include <math.h>

/* Returns a very crude approximation of Pi
   given a int: a number of iteration */
PI_API float pi_approx(int n){

  double i,x,y,sum=0;

  for(i=0;i<n;i++){

    x=rand();
    y=rand();

    if (sqrt(x*x+y*y) < sqrt((double)RAND_MAX*RAND_MAX))
      sum++; }

  return 4*(float)sum/(float)n; }
