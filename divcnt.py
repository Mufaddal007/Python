n=12
c=0
for x in str(n):
    if int(x)!=0:
        if n%int(x)==0:
            c+=1
            str(n).replace(x,'0')

print(c)
        
        
