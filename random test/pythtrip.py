i=int(input())
fin=[]
tripset=[]
for x in range(i):
    n=int(input())
    ptfound=False
    thisnum=[]
    for x in range(1,n):
        a=x**2
        for y in range(x,n):
            b=y**2
            for z in range(y,n):
                c=z**2
                if a+b==c :
                    m=0
                    mfound=False
                    for p in tripset:
                        if x%int(p[0])==0 and y%int(p[1])==0 and z%int(p[2])==0:
                            mfound=True
                            break
                    if mfound==False:
                        m=x*y*z
                        h=[x,y,z]
                        fin.append(m)
                        tripset.append(h)
                        ptfound=True
    if ptfound==False:
        thisnum.append(-1)
        tripset.append('pyth. triplet set not found')
        fin.append(-1)


for x in range(len(fin)):
    print("{}={}".format(fin[x],tripset[x]))
