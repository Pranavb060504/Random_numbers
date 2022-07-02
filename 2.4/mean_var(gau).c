#include<stdio.h>
#include"coeffs.h"
int main(){
  char*str="gau.dat";
  printf("mean:%lf, variance:%lf",mean(str),var(str));
    //Mean:-0.000417,Variance:0.999902
}
