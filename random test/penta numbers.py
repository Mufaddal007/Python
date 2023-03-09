n=10
k=2
a=[]
for x in range(1,n):
    p=int((x*(3*x-1))/2)
    pnsubk=int(((x-k)*(3*(x-k)-1))/2)
    a.append(p)
    print(p, pnsubk)
    if (p+pnsubk in a) or (p-pnsubk in a):
        print(p)
        
        
    
    
    
