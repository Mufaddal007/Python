a=[1,2,3,2,4,6,7,1,2,3,4,5,6,1,2,3]
maxc=0
c=0
for x in range(len(a)-1):
    if a[x]<a[x+1]: c+=1
    else: maxc=max(maxc, c); c=1;
maxc=max(maxc, c)
print(maxc)
