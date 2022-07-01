from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,1,20)
y1=0.5-x
y2 = 1-x
y3=1.5-x
x=np.linspace(0,1,20)
y=np.array([1]*20)
plt.plot(x,y2,color="tab:orange",label="U1+U2=t, for t<1")
plt.plot(x,y1,color="aqua",label="U1+U2=1")
plt.plot(x,y3,color="darkorchid",label="U1+U2=t, for t>1")
plt.plot(x,y,color="r")
plt.plot(y,x,color='r')
plt.axhline(xmin=-0.3, xmax=1.3)
plt.axvline(ymin=-0.3, ymax=1.3)
plt.annotate("A(1,1)",(1,1))
plt.annotate("B(1,t-1)",(1,0.5))
plt.annotate("C(t-1,1)",(0.5,1))
plt.annotate("D(1,0)",(1,0))
plt.annotate("E(0,1)",(0,1))
plt.annotate("F(t,0)",(0.5,0))
plt.annotate("E(0,t)",(0,0.5))
plt.legend()
plt.show()
