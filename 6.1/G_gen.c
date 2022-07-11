#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
#define N 1000000
int  main(void) //main function begins
{
 FILE*fp=fopen("G.dat","w");
 for(int i=0;i<N;i++){
  fprintf(fp,"%lf\n",chi(2,1));
 }
fclose(fp);
return 0;
}
