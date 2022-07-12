import matplotlib.pyplot as plt
import numpy as np
ys0i=np.loadtxt("ys0i.dat",dtype="double")
ys0j=np.loadtxt("ys0j.dat",dtype="double")
ys1i=np.loadtxt("ys1i.dat",dtype="double")
ys1j=np.loadtxt("ys1j.dat",dtype="double")
x=np.linspace(-10,10,20)
plt.plot(ys0i,ys0j,'.',color='r',label='y|s0')
plt.plot(ys1i,ys1j,'.',color='b',label='y|s1')
plt.plot(x,x)
plt.legend()
plt.grid()
plt.show()