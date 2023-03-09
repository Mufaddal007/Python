#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    s1=str(bin(n))
    s2=s1[s1.index('b')+1:]
    arr1=s2.split('0')
    
    y=0
    for x in arr1:
        if len(x)>y:
            y=len(x)
    print(y)
    
    
    
