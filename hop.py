c=[1,1,1,0,1,1,0,0,0,0]
k=3
e=100
for x in range(0,len(c),k):
        print((x+k)%len(c), c[(x+k)%len(c)])
        e=100
        x=0
        if c[0]==0:
            e-=1
        elif c[0]==1:
            e-=3
        while (x+k)%len(c)!=0:
            if c[(x+k)%len(c)]==0:
                e=e-1
            elif c[(x+k)%len(c)]==1:
                e=e-3
            x+=k
       
print(e)
    
