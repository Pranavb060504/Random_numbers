import math
with open("G.dat","r") as f1:
    a=[]
    for line in f1:
        a.append(math.sqrt(float(line)))
with open("A.dat","w") as f2:
    for i in range(0,len(a)):
        f2.write(f"{a[i]}\n")