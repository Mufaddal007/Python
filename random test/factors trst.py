a=[]
b=[]
fact=[]
mult=[]
w=101110
for x in reversed(range(1,w)):
    y=list(str(x))
    y.reverse()
    if y==list(str(x)):
        fact.append(x)
        print("chewck")
    for n in fact:
        
        for x in range(1,n+1):
            if n%x==0:
                a.append(x)
            else:
                continue
        for x in a:
            if len(str(x))==3:
                b.append(x)
        found="False"
        for x in b:
            if found=="True":
                break
            for y in b:
                if x!=y and x*y==n:
                
                    found="True"
        break           

print(fact)
print(a,b)
