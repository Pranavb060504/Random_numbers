with open("gau1.dat","r") as f1:
    with open ("gau2.dat","r")as f2:
        with open ("G.dat","w") as f3:
            a=[]
            for line in f1:
                a.append(float(line)*float(line))
            b=[]
            for line in f2:
                b.append(float(line)*float(line))
            c=[]
            for i in range(0,len(b)):
                c.append(float(a[i])+float(b[i]))    
            for i in range(0,len(c)):
                f3.write(f"{c[i]}\n")
            

                

            
                     



