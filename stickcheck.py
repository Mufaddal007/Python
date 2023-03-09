arr=[8,8,14,10,3,5,14,12]
temp=[]
while len(arr)>=1:
    temp.append(len(arr))
    mn = int(min(arr))
    arr = [int(x)-mn for x in arr if int(x)-mn!= 0] 
for x in temp:
    print(x)

