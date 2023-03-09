c=[0,0,1,0,0,1,0]
pos=0
i=0
for x in range(len(c)):
    
    if pos+1<len(c)-1 :
        if c[pos+1]==0:
            pos+=1
            i+=1
            
        elif c[pos+1]==1 :
            pos+=2
            i+=1
    
print(i)

for x in range(len(c)):
        i=0
        if pos+1<len(c)-1:
            if c[pos+2]==0:
                pos+=2
                i+=1
            elif c[pos+2]==1:
                pos+=1
                i+=1
print(i)

