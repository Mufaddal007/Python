n=int(input())
a=[1,1,2]
b=[]
i=0
while len(str(a[-1]))!=n:
    a.append(a[-1]+a[-2])
    i+=1
b.append(i+3)
    
print(b)
