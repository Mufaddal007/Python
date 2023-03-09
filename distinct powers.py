n=5
c=0
b=[]
for x in range(2,n+1):
    for y in range(2,n+1):
        if x**y not in b:
            c+=1
            b.append(x**y)

print(c)
        
