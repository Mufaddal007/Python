k=5
s=[1,2,3,4,5,6]
c=0
a=[]
for x in range(len(s)):
    for y in range(x+1,len(s)):
        if (s[x]+s[y])%3==0:
            b=[s[x],s[y]]
            a.append(b)
            c+=1
print(c)
            
