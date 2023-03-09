n=int(input())
arr=set(map(int, input().split()))
n1=int(input())
arr1=set(map(int, input().split()))
arr2=[]

for x in arr:
    if x not in arr1:
        arr2.append(x)
for x in arr1:
    if x not in arr:
        arr2.append(x)
arr2.sort()
print(arr2)
