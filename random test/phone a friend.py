n=int(input())
dict1={}
for x in range(n):
    s1=input().split()
    dict1[s1[0]]=s1[1]
arr1=[]
y=''
while y != "empty":
    s2=input()
    if s2:
        arr1.append(s2)
    elif not s2:
        y='empty'

for x  in arr1:
    if x in dict1:
        print(x+"="+dict1[x])
    else:
        print("Not found")
    
