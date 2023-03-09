a=3
b=3
c=3
n=5
arr=[]
arr3=[]
for x in range(1,a+1):
    for y in range(1,b+1):
        for z in range(1,c+1):
           arr1=[]    
           arr1.append(x)
           arr1.append(y)
           arr1.append(z)
           arr.append(arr1)

for x in arr:
    i=0
    for y in x:
        i+=y

    if i != n:
        arr3.append(x)
    else:
        arr3.append("Not mentioned")
    
          
#print(arr)

print(arr3)

       
