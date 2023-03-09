n=10
k=8
c=0
if k==2:
    for x in range(1,n):
        chk=str(bin(x))[list(bin(x)).index('b')+1:]
        print(chk)
        chk1=chk[::-1].ltrim('0')
        if chk==chk1 and str(x)==str(x)[::-1]:
            c+=x
            print(c)
    
        
elif k==8:
    for x in range(1,n):
    
        chk=str(oct(x))[list(oct(x)).index('o')+1:]
        chk1=chk[::-1].ltrim('0')
        if chk==chk1 and str(x)==str(x)[::-1]:
    
            c+=x

print(c)       
