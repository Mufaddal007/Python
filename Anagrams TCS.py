s='condingisfun'
n=11
cnt=0
n1=n//2
while(n1>=1):
    a=list(s[:n1])
    b=list(s[n1:])
    a1=list(set(a))
    c=0
    for x in a1:
        if x in b:
            c+=min(a.count(x), b.count(x))
    cnt=max(cnt, c)
    n1-=1
while(n1<n):
    
    a=list(s[:n1])
    b=list(s[n1:])
    a1=list(set(a))
    c=0
    for x in a1:
        if x in b:
            c+=min(a.count(x), b.count(x))
    cnt=max(cnt, c)
    n1+=1
print(cnt)
            
    
