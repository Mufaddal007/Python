a=[[21,22,23,24,25],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]]
c=0
b=[]
d=[]
for x in range(len(a)):
    b.append(a[x][x])
    d.append(a[x][-x-1])
    c+=a[x][x]
    c+=a[x][-x-1]
c-=a[]
print(b,d)
print(c)
