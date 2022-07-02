#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
gaussian("gau1.dat", 1000000);

//Uniform random numbers
gaussian("gau2.dat", 1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}
