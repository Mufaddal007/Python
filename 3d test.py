a=[]
for x in range(6):
    a.append(input().split())
sums=[]
for k in range(4):
    for z in range(4):
        c=0
        for x in range(3):
            if z!=3:
                c+=int(a[x+k][z])
            c+=int(a[x+k][z+1])
            if z!=5:
                c+=int(a[x+k][z+2])
        sums.append(c)
sums.sort()
print(sums[15])        
print(sums)
