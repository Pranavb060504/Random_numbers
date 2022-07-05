#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a,t;
FILE*fp=fopen("bernoulli.dat","w");
for(int i=0;i<10000;i++)
{
    a=rand();
if(a%2==0){
    t=1;
}
else{
    t=-1;
}
 fprintf(fp,"%d\n",t); 
}
fclose(fp);
}