#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
#define N 1000000
int main(){
    FILE*fp=fopen("G.dat","r");
    FILE*f1=fopen("A.dat","w");
    double t;
    for(int i=0;i<N;i++){
        fscanf(fp,"%lf",&t);
        t=sqrt(t);
        fprintf(f1,"%lf",t);
    }
    fclose(fp);
    fclose(f1);
    return 0;
}
