#!/bin/python3

import sys


a =[3,2,1]
c=0
for x in range(len(a)-1,0,-1):
    for y in range(x):
        if a[y]>a[y+1] :
            a[y],a[y+1]=a[y+1],a[y]
            c+=1
        
print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(c,a[0],a[len(a)-1]))
