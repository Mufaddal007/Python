n=4
c=0
i=0
while i<=n:
    if i%2==0:
        c+=1
        i+=1
    elif i%2!=0:
        c*=2
        i+=1
print(c)
