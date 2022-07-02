#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math

#if using termux
#import subprocess
#import shlex
#end if


maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('G.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def G_pdf(x):
    if x<0:
        x=0
    if 0<=x<=1:
        x=math.pi*x/2
    if 1<x<=2:
        x=1/(2*math.sqrt(x-1)) -1/(4*math.sqrt(x-1)*math.sqrt(2-x)) -(-2*x+3)/(4*math.sqrt(3*x-2-(x*x)))
    else:
        x=0
    return x
    
pdf_formula = []
for i in range(len(x)):
    pdf_formula.append(G_pdf(x[i]))

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,pdf_formula)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_pdf.pdf')
#plt.savefig('../figs/gauss_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
#plt.show() #opening the plot window
