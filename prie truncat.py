n=int(input())
c=0
for x in range(11,n):
    prime=False
    for y in range(1,x):
        if x%y==0:
            prime=True
    i=0
    if prime:
        rprime=False
        lprime=False
        for w in range(len(str(x))):
            s=int(str(x)[w:])
            for z in range(1,s):
                if s%z==0:
                    i+=1

        if i==len(str(x)):
            rprime=True

    
        i=0
        for w in reversed(range(len(str(x)))):
            s=int(str(x)[:w])
            for z in range(1,s):
                if s%z==0:
                    i+=1

        if i==len(str(x)):
            lprime=True

        if lprime and lprime:
            c+=x
print(c)
