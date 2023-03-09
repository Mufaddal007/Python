maxint=1E9+7
from itertools import combinations as ic
a=[1,2,3,2,4,6,7]
b=[]
gcdglobal=1
def findgcd(x):
    for z in range(min(x),0,-1):
        flag=1
        for y in x:
            if y%z!=0: flag=0; break;
        if flag: return z

for x in range(1,len(a)):
    b+=list(ic(a,x))
for x in b:
    i=findgcd(x)    
    gcdglobal*=i
print(gcdglobal%maxint)


