n1=10
k=2
c=''
c1=0

for n in range(1,n1):
    n2=n
    if str(n)==str(n)[::-1]:
        while n>0:
            c+=str(n%k)
            n=(n-n%k)//k
        pal=c[::-1]
        if pal==pal[::-1]:
            c1+=n2
            print(n2)
            
print(c1)  
