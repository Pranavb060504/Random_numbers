#include<stdio.h>
int main(){
    int count=0;
    double sum=0;
    double squares=0;
    double t;
    double a,b;
    FILE*fp=fopen("uni.dat","r");
    while(fscanf(fp, "%lf", &t)!=-1){
        count+=1;
        sum=sum+t;
        squares=squares+(t*t);
    }
    a=sum/count;
    b=(squares/count)-(a*a);

    printf("Mean:%lf,Variance:%lf",a,b);
    fclose(fp);
}
