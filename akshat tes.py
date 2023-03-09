import math
n = int(input())
a = []
for x in range(n) :
    a.append(input())
a.sort()
print("After Sorting:- {} ".format(a))
b = []
for i in range(int(len(a)/2)+1):
    b.append(a[i])
    b.append(a[len(a)-1-i])
if n%2 != 0:
    b.remove(b[-1])
    print(b)
    
else:                    
    print(b)
