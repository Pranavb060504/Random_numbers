#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math

#if using termux
# import subprocess
# import shlex
# #end if


maxrange=20
maxlim=5.0
x = np.linspace(0.01,maxlim,maxrange)#points on the x axis
with open("Gamma.dat","w") as f1:
    for y in x:
        f1.write(f"{y}\n")
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('Ray.dat',dtype='double')	
def Gam_pdf(y):
    return (0.5*(1-math.sqrt(y/(y+2))))
vec_Gam_pdf = scipy.vectorize(Gam_pdf)

plt.plot(x[0:(maxrange)].T,randvar,'o')
# plt.plot(x,vec_Gam_pdf(x))
# plt.semilogy(x[0:(maxrange)].T,randvar,'o')
# plt.semilogy(x,vec_Gam_pdf(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
# plt.savefig('../figs/gauss_pdf.pdf')
# plt.savefig('../figs/gauss_pdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
