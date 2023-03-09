n=1
a=[]
for x in range(n):
    n1=int(input())
    b=[]
    c=0
    
    for x in range(1,n1):
        if n1%x==0:
            c+=x
            b.append(x)
    if c==n1:
        a.append("YES")
    else:
        a.append("NO")
    print(b)
for x in a:
    print(x)    

