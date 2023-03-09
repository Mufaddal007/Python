n=int(input())
a=[]
for y in reversed(range(n)):
    s=''
    for x in range(n,y,-1):
        s+=chr(64+x).lower()
    
    s2=s[:-1]
    s3=s2[::-1]
    s4=list(s+s3)
    s5='-'.join(s4)
    s1=s5.center(4*n-3,'-')
    a.append(s1)
    print(s1)
a.reverse()
for x in range(1,n):
    print(a[x])
    
