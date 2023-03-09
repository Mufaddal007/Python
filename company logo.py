s='google'.split()

c1=[]
s1=[]

c2=[]

for x in s:
    if x not in s1:
        s1.append(x)
        c1.append(s.count(x))
s11=s1
s1.sort()
i=0
for x in s11:
    c2.insert(s1.index(x),c1[i])
    i+=1
print(s1)
print(c1)
print(s11)
print(c2)

    
    
        
    
