a=['ooo','xxx','oxo']
a1=sum([a[x].count('x') for x in range(len(a))])
a2=sum([a[x].count('o') for x in range(len(a))])
print('x.count=',a1,'          o.count=',a2)

