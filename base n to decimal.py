chars=['A','B','C', 'D','E', 'F']
s=input('Enter the number you want in decimal: ')
k=int(input('From which base system?'))
bd=s[:s.index('.')]
ad=s[s.index('.')+1:]
d=0
for x in range(len(bd)):
    if bd[x].isdigit():
        d+=int(bd[x])*pow(k,len(bd)-x-1)
        continue
    d+=(10+chars.index(bd[x]))*pow(k,len(bd)-x-1)
for x in ad:
    if ad[x].isdigit():
        d=int(ad[x])*pow(k,-x)
        continue
    d=(10+chars.index(ad[x]))*pow(k,-x)
print(d)
        
        
