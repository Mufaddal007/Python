s='Ab1'
schar=['!','@','#','$','%','^','&','*','(',')','-','+']
uc=lc=dc=sc=0
l=len(s)
for x in s:
    if x in schar:
        sc+=1
    elif x.isdigit():
        dc+=1
    elif x.isupper():
        uc+=1
    elif x.islower():
        lc+=1

check=(dc>=1) and (lc>=1) and (dc>=1) and (len(s)>=6)
c=0
if dc==0:
    c+=1
if lc==0:
    c+=1
if uc==0:
    c+=1 
if sc==0:
    c+=1
if l+c<6:
    c+=6-(l+c)
print(c)    
    
    
