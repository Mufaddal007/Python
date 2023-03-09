import math

n1=int(input())
a=[]
for x in range(n1):
    n=int(input())
    final=str(int(math.pow(2,n)))
    c=0
    for y in final:
        c+=int(y)
    print(final) 
    a.append(c)
for x in a:
    print(x)
