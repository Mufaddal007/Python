k=3
arr=[4,2,6,1,10]
pc=1
chap1=[]
spe=0
for x in arr:
    chap=[]
    i=0
    for y in range(1,x+1):
        if i<k:
            chap.append(y)
            i+=1
            
        elif i==k:
            chap1.append(chap)
            
            if pc+arr.index(x) in chap:
                spe+=1
            pc+=1
            chap=[y]
            i=1
           
    t=pc+arr.index(x)   
    if t in chap:
            spe+=1
    chap1.append(chap)     
print(spe)
        
        
        
        
    
        
    
        
