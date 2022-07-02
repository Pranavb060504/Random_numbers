with open("uni1.dat","r") as f1:
    with open ("uni2.dat","r")as f2:
        with open ("T.dat","w") as f3:
            a=[]
            for line in f1:
                a.append(line)
            b=[]
            for line in f2:
                b.append(line)
            c=[]
            for i in range(0,len(b)):
                c.append(float(a[i])+float(b[i]))    
            for i in range(0,len(c)):
                f3.write(f"{c[i]}\n")
        

                

            
                     



