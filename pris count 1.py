n=5
m=19
t=2
if m>n:
    m=m%n-1
else:
    m=m-1
#for x in range(1,m):
#    if s+1>n:
#        s=1
#    else:
#        s+=1
#print(m)
#print(s)
    
if m+t>n:
    t=m+t-n
else:
    t=m+t
    
print(t)
