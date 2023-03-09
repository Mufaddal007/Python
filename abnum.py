n1=int(input())
a=[]
final=[]
for x in range(n1):
    n=int(input())
    for x in range(1,n):
        c=0
        for y in range(1,x):
            if x%y==0:
                c+=y
        if c>x:
            a.append(x)
    check=False
    for x in range(len(a)-1):
        
        for y in range(x+1) :
            if a[x]+a[y]==n and n%a[x]==0 and n%a[y]==0:
                
                check=True
                break
            
            
    if check:
        final.append("yes")
            
    else:
        final.append("No")

      
for x in final:
    print(x)
