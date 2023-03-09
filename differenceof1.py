a=[1,2,2,3,1,2]
dif1=[]
for x in range(len(a)):
    for y in range(x+1,len(a)):
        if a[x]-a[y]<=1:
            
            if not [a[x],a[y]] in dif1 and a[x]!=a[y]:
                
                dif1.append([a[x],a[y]])
print(dif1)
