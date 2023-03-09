a=10
b=20
c=0
i=0
e=0
n=max(a,b)
while(n>>i):
    d=((a>>i)&1) + ((b>>i)&1) + c
    if d==0:
        c=0
    elif d==1:
        c=0
        e|=1<<i
    elif d==2:
        c=1
    else:
        c=1
        e|=1<<i
    i+=1
e|=(c<<i)
print(e)
