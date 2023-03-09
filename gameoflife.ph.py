a=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
a1=[['' for y in range(len(a[0]))] for x in range(len(a))]
print()
ior=len(a)-1
ioc=len(a[0])-1
i=j=0
surrounds=[]
numberofones=[]
def change_state(e,b):
    if e==1 and 1<b<4: return 1
    elif e==1 and (b<2 or b>3): return 0 
    elif e==0 and b==3: return 1
    return e
    
for i in range((ior+1)):
    for j in range(ioc+1):
        if i==0 or j==0 or i==ior or j==ioc:
            b=[]
            if i==0 and 1<=j<=ioc-1:b=[a[i][j-1],a[i][j+1],a[i+1][j-1],a[i+1][j], a[i+1][j+1]]
            elif i==ior and  1<=j<=ioc-1: b=[a[i][j-1], a[i][j+1], a[i-1][j-1], a[i-1][j], a[i-1][j+1]]
            elif j==0 and 1<=i<=ior-1:b=[a[i-1][j], a[i+1][j], a[i-1][j+1],a[i][j+1], a[i+1][j+1]]
            elif j==ioc and 1<=i<=ior-1: b=[a[i-1][j],a[i+1][j], a[i-1][j-1], a[i][j-1], a[i+1][j-1]]
            elif i==0 and j==0: b=[a[0][1], a[1][0], a[1][1]]
            elif i==0 and j==ioc: b= [a[0][-2],a[1][-1], a[1][-2]]
            elif i==ior and j==0: b=[a[-1][1],a[-2][0],a[-2][1]]
            elif i==ior and j==ioc: b=[a[-1][-2],a[-2][-1],a[-2][-2]]
            surrounds.append([a[i][j],b])
            numberofones.append(b.count(1))
            a1[i][j]=change_state(a[i][j], b.count(1))
        else:
            c=[a[i-1][j-1], a[i-1][j], a[i-1][j+1], a[i][j-1], a[i][j+1], a[i+1][j-1], a[i+1][j],a[i+1][j+1]]
            surrounds.append([a[i][j],c])
            numberofones.append(c.count(1))
            a1[i][j]=change_state(a[i][j], c.count(1))
[print(x) for x in a1]


            



