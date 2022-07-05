from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math
import mpmath
import scipy
def Q(x):
	return mpmath.erfc(x/math.sqrt(2))/2
def P(x):
    return Q(x)
a=np.linspace(0,10,50)
p=np.loadtxt("Pgen.dat",dtype="double")
with open ("aG.dat","w") as f1:
    for i in range(0,50):
        f1.write(f"{a[i]}\n")   
simlen = int(1e4) 
vec_T_pdf = scipy.vectorize(P)
plt.plot(a,p,'o')
plt.plot(a,vec_T_pdf(a))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.show()