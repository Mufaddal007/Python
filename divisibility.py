w=int(input())
a=[]
for x in range(w):
    n=int(input())
    i=0
    
    num=0
    check=True
    while check==True:
        c=0
        i+=1
        for x in range(1,n+1):
            if i%x==0 :
                c+=1
                
        if c==n:
            check=False
            a.append(i)
            
    
for x in a:
    print(x)

