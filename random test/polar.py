import math
import cmath

c=input()
arr=[]
for x in c:
    if x.isdigit():
        a=c[:c.index(x)-1]
        b=c[c.index(x)-1:-1]

x=int(a)
y=int(b)

a=pow(x,2)
b=pow(y,2)

r=math.sqrt(a+b)
p=cmath.phase(complex(c))

print(r)
print(p)
