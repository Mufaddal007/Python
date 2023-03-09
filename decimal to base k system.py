chars=['A','B','C', 'D', 'E', 'F']
while 1:
    ad=[]
    bd=[]
    n=float(input())
    k=int(input())
    n1=int(str(n)[:str(n).index(".")])
    n2=n-int(n)
    r=n
    i=0
    while n2!=1 and i<4:
        
        
        n2=n2*k
        ad.append(str(int(n2)))
        n3='0.'+str(n2)[str(n2).index('.')+1:]
        n2=float(n3)
        i+=1
     
    while n1>=k:
        r=n1%k
        n1=int((n1-r)/k)
        if r>9:
            bd.append(chars[r%10])
        else :
            bd.append(str(r))

    if n1>9:
        bd.append(chars[n1%10])
    else:
        bd.append(str(n1))
    bd.reverse()
    s=("".join(bd))+'.'+("".join(ad))
    print(s)
    
        

