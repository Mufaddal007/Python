arr=input().split()
arr.sort()
cnt=0
fin=[]
for x in arr:
    if int(x)>=int(arr[0]):
        cnt+=1
fin.append(cnt)
while len(arr)>1:
    arr1=[]
    for x in arr:
        if int(x)>arr[0]:
            arr1.append(int(x)-int(arr[0]))
    arr=arr1
    fin.append(len(arr1))
for x in fin:
    print(x)
