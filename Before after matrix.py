before=[[1,2,3],[2,2,1]]
after=[]
m=2
n=3
for x in range(m):
    temp=[]
    for y in range(n):
        if y==0 and x==0: temp.append(before[0][0])
        elif x==0 and y>0: temp.append(before[0][y]+temp[y-1])
        elif x>0 and y==0: temp.append(before[x][0]+after[x-1][0])
        else: temp.append((temp[y-1]+after[x-1][y]-after[x-1][y-1])+before[x][y])
    after.append(temp)
print(after)
