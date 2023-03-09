n1,k1,m1=input().split()
n=int(n1)
k=int(k1)
m=int(m1)
rw=n%k
c=int((n-(n%k))/k)
    
w=c
b=c
while w>=m:
    rw+=c%2
    w=c=int((c-c%m)/m)
    b+=c
        

if w+rw>=m:
    t=w+rw
    c=int((t-(t%m))/m)
    b+=c
print(b)
        
