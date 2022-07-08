#include<stdio.h>
int main()
{    int t;
    float a;
    FILE*fp=fopen("gau.dat","r");
    FILE*f1=fopen("bernoulli.dat","r");
    FILE*f2=fopen("Y.dat","w");
    for(int i=0;i<1000000;i++){
        fscanf(fp,"%f",&a);
        fscanf(f1,"%d",&t);
        fprintf(f2,"%f\n",a+5*t);
    }
    fclose(fp);
    fclose(f1);
    fclose(f2);

}
