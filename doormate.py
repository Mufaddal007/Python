s=''
n1,m1=input().split()
n=int(n1)
m=int(m1)
a=[]
for x in range(int((n-1)/2)):
    y=3*(1+(2*x))
    s='-'*int(((m-y))/2)
    s+=(2*x+1)*'.|.'
    s+='-'*int(((m-y))/2)
    a.append(s)
    print(s)
a.reverse()
s1=('-'*int((m-7)/2))+'WELCOME'+('-'*int((m-7)/2))
print(s1)   
for x in a:
    print(x)
    
