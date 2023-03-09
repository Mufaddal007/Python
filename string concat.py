from itertools import permutations
s=input()
b=[]
for x in range(1,len(s)+1):
    a=list(permutations(s,x))
    for y in a:
        z=list(y)
        z.sort()
        b.append(''.join(z))
d=list(set(b))
d.sort()
print(d)

        
