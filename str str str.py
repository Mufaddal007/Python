s='abcd'
a=tuple(s)
b=list(a)
for z in range(len(s)):
    c=[]
    for x in a:
        b.remove(x)
        for y in b:
           s1=x+y
           c.append(s1)
    
    print(c)
        
    
    
