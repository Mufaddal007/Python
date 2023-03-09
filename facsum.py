import math
n=int(input())
a=0
    
for x in range(10,n):
    c=0
    for y in str(x):
        c+=math.factorial(int(y))
    if c%x==0:
        a+=x


print(a)
