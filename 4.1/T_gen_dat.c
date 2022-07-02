
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
	FILE *fp = fopen("T.dat", "w");
	for (int i = 0; i < 1000000; i++) {
		double u1 = (double)rand()/RAND_MAX;
		double u2 = (double)rand()/RAND_MAX;
		fprintf(fp, "%lf\n", u1 + u2);
	}
	fclose(fp);
	return 0;	
}
        

                

            
                     



