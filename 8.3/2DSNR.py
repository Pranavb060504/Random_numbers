import numpy as np
import matplotlib.pyplot as plt
import mpmath
import scipy
x=np.linspace(0.01,10,50)
with open ("xlp.dat","w") as f1:
    for item in x:
        f1.write(f"{item}\n")
def Q(x):
    return 0.5*mpmath.erfc(x)
z=scipy.vectorize(Q)
y=np.loadtxt("2dSNR.dat",dtype="double")
plt.plot(x,z(x),label="Theoretical")
plt.plot(x,y,".",label="Simulation")
plt.legend()
plt.grid()
plt.show()



        

