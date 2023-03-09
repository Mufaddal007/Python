ar=[10,20,20,10,10,30,50,10,20]
a=[]
b=[]
c=0
for x in ar:
    if not x in a:
        a.append(x)
        b.append(ar.count(x))
print(a)
print(b)
for x in b:
    if x%2!=0:
        x-=1
        c+=x/2
    elif x%2==0:
        c+=x/2

print(int(c))
