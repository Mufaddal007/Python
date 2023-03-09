n=int(input())
arr=[]
for x in range(n):
    s=input().split()
    if s[0]=="append":
        arr.append(int(s[1]))
       
    elif s[0]=="appendleft":
        arr.insert(0, int(s[1]))
       
    elif s[0]=="pop":
        del arr[-1]
        
    elif s[0]=="popleft":
        del arr[0]
        
s=""
for x in arr:
    s+=str(x)
    s+=" "
print(s)       
