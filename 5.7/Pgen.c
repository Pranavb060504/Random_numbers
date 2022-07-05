#include<stdio.h>
int main()
{
    FILE*fp=fopen("aG.dat","r");
    FILE*f1=fopen("bernoulli.dat","r");
    FILE*f2=fopen("gau3.dat","r");
    FILE*f3=fopen("Pgen.dat","w");
    double p1=0,p2=0,y;
    double t,r,p,x;
    int count1=0,count2=0;
    while(fscanf(fp,"%lf",&t)!=EOF){
        while(fscanf(f1,"%lf",&r)!=EOF){
            fscanf(f2,"%lf",&p);
            y=t*r+p;
            if(r==1){
                count1+=1;
            }
            if(r==-1){
                count2+=1;
            }
            if(y>0 && r==-1){
                p1=p1+1;
            }
            if(y<0 && r==1){
                p2=p2+1;
            }  
        }
        x=(double)(0.5*p1)/count2+(double)(0.5*p2)/count1;
        p1=0;
        p2=0;
        f2 = fopen("gau3.dat","r");
        f1=fopen("bernoulli.dat","r");
        fprintf(f3,"%lf\n",x);
    }
    fclose(fp);
    fclose(f1);
    fclose(f2);
    fclose(f3);
}