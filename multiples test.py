#!/bin/python3
import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=[]
    c=0
    final=[]
    a.append(1)
    a.append(2)
    for x in range(1,n):
        a.append(a[-1]+a[-2])
    for x in a:
        if x%2==0 and x<n:
            final.append(x)
            c+=x
    print(c)
    
