n=int(input())
a=[]
for x in range(n):
    a.append(input().split())
i=0
ld=0
rd=0
for x in range(len(a)):
    
    for y in range(len(a)):
        if x+y<len(a) and i<len(a):
            
            i+=1
            ld+=int(a[x+y][y])
for x in range(len(a)):
    for y in reversed(range(len(a))):
        if (x+y+1)==len(a):
            rd+=int(a[x][y])
        
        
fin=abs(ld-rd)
print(fin)
       
