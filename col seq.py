t=1
d=[]
for x in range(t):
    c=0
    e=0
    n1=int(input())
    b=[]
    for y in range(2,n1):
        n=y
        a=[n]
        while n!=1:
            if n%2==0:
                n=n/2
                a.append(int(n))
            elif n%2!=0:
                n=3*n+1
                a.append(int(n))
        print(a)        
        if len(a)>=e:
            e=len(a)
            c=y
            print(e,c)
    d.append(c)
for x in d:
    print(x)
