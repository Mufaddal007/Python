mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]

for x in range(3):
    for y in range(3):
        if x-1<0:
            mat[x-1][y]=0
        if x+1>2:
            mat[x+1][y]=0
        if y-1<0:
            mat[x].insert(y-1,0)
        if y+1>2:
            mat[x].insert(y+1,0)
        print(mat[x][y], mat[x][y-1], mat[x][y+1], mat[x+1][y], mat[x-1][y] )
