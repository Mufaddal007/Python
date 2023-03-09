n=20
a=22
b=7
c=[]
for x in range(n):
    if a<7: a*=10; c.append(a//7); a=a%b
    else: c.append(a//7); a=a%b
print(c)
    
    
