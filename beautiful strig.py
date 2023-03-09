s='bcxz'
s1=s[::-1]
a=[]
b=[]
c=len(s)
for x in range(len(s)-1):
    a.append(abs(ord(s[x])-ord(s[x+1])))
for x in reversed(range(1,len(s))):
    b.append(abs(ord(s[x])-ord(s[x-1])))
chk=True
for x in range(len(a)):
    if a[x]!=b[x]:
        chk=False
        break
        
if chk:
    print('Funny')
else :
    print('Not Funny')
print(a)
print(b)
