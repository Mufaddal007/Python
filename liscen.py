name=input()
n=int(input())
s1=input().split()
s1.append(name)
s1.sort()
arr1=[]
for i in range(n):
    arr3=[]
    for x in range(i,len(s1),n):
        arr3.append(s1[x])
    arr1.append(arr3)
z=0
for x in arr1:
    if name in x:
        s2=x[:x.index(name)]
        z=20*len(s2)+20
        print(z)

