n=int(input())
a=[]
for x in range(n):
    n1,k=input().split()
    c=0
    
    b=[]
    for x in range(1,int(n1)+1):
        for y in range(x+1,int(n1)+1):
            if x&y<int(k):
                c+=1
                b.append(x&y)
    b.sort()
    if not b:
        a.append(0)
    else:
        a.append(b[-1])        
for x in a:
    print(x)
    

    

