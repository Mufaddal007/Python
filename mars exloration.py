s='SOSSPSSQSSOR'
c=0
for x in range(0,len(s),3):
    if s[x]!='s':
        c+=1
    if s[x+1]!='o':
        c+=1
    if s[x+2]!='s':
        c+=1

print(c)
    
