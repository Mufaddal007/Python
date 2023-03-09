import math
n=17
c=0
for x in range(n+1):
    c+=bin(x).count('1')
print(c)
print()
a=0
n1=int((math.log(n, 2)))+1
for x in range(n1+1):
    a+=((n+1)//(2**(x+1)))*(2**x)
    if (n+1)%(2**(x+1))>(2**x):
        a+=(n+1)%(2**x)
    
print(a)
