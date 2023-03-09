wid=[1,2,2,2,1]
s=[[2,3],
[1,4],
[2,4],
[2,4],
[2,3]]
for x in s:
    b=wid[x[0]:x[1]+1]
    b.sort()
    print(b)
    print(b[0])
