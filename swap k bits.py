x=47
temp1=x
p1=1
p2=5
n=3

#first approach

if p1!=0:
    m=1<<(p1-1)
    m=m | (m-1)
    s1=x&m
else: s1=None

m=1<<(n-1)
m=m | m-1
temp=m
s2=(x>>p1) & m
s2<<=p2

if not (p2-(p1+n)-1)<0:
    m=1<<(p2-(p1+n)-1)
    m=m | (m-1)
    s3=(m<<(p1+n))&x
else: s3=None

s4=(x>>p2) & temp
s4<<=p1

x>>=(p2+n)
x<<=(p2+n)

if s1 and s3: x=x|s2|s3|s4|s1
elif s1 and not s3: x=x|s1|s2|s4
elif not s1 and s3: x=x|s2|s3|s4
else: x=x|s2|s4

print(temp1, x, bin(temp1),bin(x))


#second appraoch is much easier
x=47
print(x, bin(x), end=" ")
p1=1
p2=5
n=3

m=(1<<(n-1))| ((1<<(n-1))-1)
bs1, bs2=m&(x>>p1), m&(x>>p2)
x&=~((m<<p1)|(m<<p2))
x=x|(bs1<<p2)|(bs2<<p1)
print(x, bin(x))
