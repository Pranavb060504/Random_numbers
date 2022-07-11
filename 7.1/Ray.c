#include<stdio.h>
#include"coeffs.h"
#include<math.h>
int main(){
    FILE*fp=fopen("Gamma.dat","r");
    FILE*f1=fopen("Ray.dat","w");
    double t,u;
    while(fscanf(fp,"%lf",&t)!=EOF){
        double y=0;
        int count0=0,count1=0;
        FILE*f2=fopen("bernoulli.dat","r");
       while(fscanf(f2,"%lf",&u)!=EOF)
        {
            y= Ray(t)*u+gau();
            if(u==1){
            count0+=1;
            }
            if(y<0 && u==1){
                count1+=1;
            }
        }
        double p=(double) count1/count0;
        fprintf(f1,"%lf\n",p);
        fclose(f2); 
    }
    fclose(f1);
    fclose(fp);
}