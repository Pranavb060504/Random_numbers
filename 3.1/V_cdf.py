#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpmath as mp
#if using termux
import subprocess
import shlex
#end if
def V_cdf(x):
	if x>=0:
		return 1-np.exp(-x**2/2.0)
	else:
		return 0


x = np.linspace(-20,20,30)#points on the x axis
simlen = int(999963) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('V.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list	
plt.plot(x.T,err)#plotting the CDF
plt.plot(x.T,err,'o')
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(["Numerical","Theory"])


#if using termux
plt.savefig('./V_cdf.pdf')
plt.savefig('./V_cdf.eps')
subprocess.run(shlex.split("termux-open ../figs/V_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window