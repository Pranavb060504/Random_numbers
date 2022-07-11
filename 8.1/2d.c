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
}
int main(){
    vec s0,s1;
    s0.i=1;
    s0.j=0;
    s1.i=0;
    s1.j=1;
    int a=10;
    FILE*fp=fopen("ys0i.dat","w");
    FILE*f1=fopen("ys0j.dat","w");
    FILE*f2=fopen("ys1i.dat","w");
    FILE*f3=fopen("ys1j.dat","w");
    for(int i=0;i<N;i++){
        vec y;
        vec n;
        n.i=gau();
        n.j=gau();
        int x=bl();
        if(x==1){
            y=sum(sp(s1,a),n);
        }
        if(x==-1){
            y=sum(sp(s0,a),n);
        }
        if(y.i>y.j && x==1){
            fprintf(fp,"%lf\n",y.i);
            fprintf(f1,"%lf\n",y.j);
        }
        if(y.i<y.j && x==-1){
            fprintf(f2,"%lf\n",y.i);
            fprintf(f3,"%lf\n",y.j);
        }
    }
    fclose(fp);
    fclose(f1);
    fclose(f2);
    fclose(f3);
}
