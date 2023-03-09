arr='1 2 3 4 3 3 2 1'.split()
arr.sort()
print(len(arr))
while len(arr)>1:
    
    temp=[]
    for x in range(len(arr)):
        y=int(arr[x])-int(arr[0])
        if y>0:
            temp.append(y)
    arr=temp
   
    print(len(temp))
    
