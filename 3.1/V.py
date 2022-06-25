import math
with open("uni.dat","r") as f1:
    with open("V.dat","w") as f2:
        for line in f1:
            if(1-float(line)>0):
                f2.write(f"{-2*math.log(1-float(line))}\n")
