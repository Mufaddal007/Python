s=input()
a=s[0]
j=2
i=len(a)
b=[]
flag=1
while(i<len(s)):
    if int(a)+1==int(s[i:i+len(a)]):
        b.append(a)
        a=s[i:i+len(a)]
        i+=len(a)
        
    else:
        c=s[i:i+len(a)+1]
        
        if int(a)+1==int(c):
            b.append(a)
            b.append(c)
            a=c
            i+=len(a)
        else:
            a=s[0:j]
            j+=1
            i+=1
            #print('extending  starting substring {}'.format(a))
    if j>3: break

if b[-1]==s[-len(b[-1]):]: print('Magical')
else: print('Not Magical')
print(b)
    
