#!/bin/python3





n = 100
a=[2,3,5,7]
sum1=0

for x in range(2,n):
    if x%2!=0 and  x%3!=0 and  x%5!=0 and x%7!=0:
        a.append(x)
for x in a:
    sum1+=x
    
print(a)

