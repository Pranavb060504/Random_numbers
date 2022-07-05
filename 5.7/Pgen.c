#include<stdio.h>
int main()
{
    FILE*fp=fopen("aG.dat","r");
    FILE*f3=fopen("Pgen.dat","w");
    double p1,p2,y;
    double t,r,p,x;
    while(fscanf(fp,"%lf",&t)!=EOF){
        p1=0;
        p2=0;
        int count1=0;
        int count2=0;
        FILE*f1=fopen("bernoulli.dat","r");
        FILE*f2=fopen("gau3.dat","r");
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
        x=(0.5*p1)/count2+(0.5*p2)/count1;
        fprintf(f3,"%lf\n",x);
         fclose(f1);
         fclose(f2);
    }
    fclose(fp);
    fclose(f3);
}