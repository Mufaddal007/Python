mat=[[1,1,1,1,1],[2,2,2,2,2],[3,8,6,7,3],[4,4,4,4,4],[5,5,5,5,5]]
temp=[]
k=2
for i in  range(len(mat)-(k-1)):
    for j in range(len(mat)-(k-1)):
        temp=[]
        for a in range(i,i+k):
            temp.append(mat[a][j:j+k])
            
            #for b in range(j,j+3):
            #    temp1.append(mat[a][b])
            #temp.append(temp1)
            print(temp[-1])
        print()

#print()
#[print(x) for x in temp]
        
