#include<stdio.h>
#include"coeffs.h"
#define N 10000
struct vec{
double i;
double j;
};
typedef struct vec vec;
vec sum(vec v1,  vec v2){
  vec v3;
  v3.i=v1.i+v2.i;
  v3.j=v1.j+v2.j;
  return v3;
}
vec sp(vec v1,double k){
    vec v3;
    v3.i=v1.i*k;
    v3.j=v1.j*k;
    return v3;
}
int main(){
    FILE*fp=fopen("xlp.dat","r");
    FILE*f1=fopen("2dSNR.dat","w");
    double t;
    vec s0,s1;
    s0.i=1;
    s0.j=-1;
    s1.i=-1;
    s1.j=1;
    while(fscanf(fp,"%lf",&t)!=EOF){
        int count0=0,count1=0;
        for(int p=0; p<N; p++){
        vec y;
        vec n;
        n.i=gau();
        n.j=gau();
        int x=bl();
        if(x == 1){
            y=sum(sp(s1,t),n);
        }
        if(x==-1){
            y=sum(sp(s0,t),n);
        }
        if(x==-1 && (y.i<y.j)){
            count0+=1;
        }
        if(x==-1){
            count1+=1;
        }
    }
    double u;
        u=(double)count0/count1;
        fprintf(f1,"%lf\n",u);
    }
    fclose(f1);
    fclose(fp);
}