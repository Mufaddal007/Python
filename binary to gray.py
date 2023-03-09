import math
a=7
c=0
n=int(math.log(a,2))+1
c|=a&(1<<(n-1))


# binary to gray
for x in range(n-1):
    b=(((a>>x)&1)^((a>>(x+1))&1))
    c|=(b<<x)
print(bin(c))

# gray to binary
c=3
b=c>>(n-1)
n=math.ceil(int(math.log(c,2)))+1
print(n)
newc=c|(b<<(n-1))

for x in range(n-2,-1,-1):
    b1=(c>>x)&1
    print(b1)
    b=b^b1
    newc=newc|(b<<(x))
print(newc)




