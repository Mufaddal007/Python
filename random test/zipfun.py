n=3
arr=[]
for x in range(n):
    s=list(map(float, input().split()))
    arr.append(s)
arr2=list(zip(*arr))
for x in arr2:
    c=sum(x)/3
    print(c)


