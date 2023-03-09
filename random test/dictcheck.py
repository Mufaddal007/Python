d={}
for x in range(4):
    name=input()
    score=input()
    d[name]=score
f=[]
t=[]
for x in d:
    chk=list(x)
    chk.insert(0,d[x])
    str1="".join(chk)
    f.append(str1)
f.sort()
for x in f:
    chk=list(x)
    chk.replace(0,"")
    str2="".join(chk)
    t.append(str2)
print(t)
    

    
