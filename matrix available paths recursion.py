a=[[1,1,3,2,1],[3,2,2,1,2],[1,3,3,1,3],[1,2,3,1,2],[1,1,1,3,1]]
n=5
i=0
j=0
c=0
a1=[]
def findpath(i,j,c):
    if i==n or j==n: return;
    elif i==n-1 and j==n-1: c+=a[i][j]; a1.append(c);
        #print('path found',c); 
    elif a[i][j]==1:
        c+=a[i][j];
        #print(i,j);
        findpath(i, j+1,c);
    elif a[i][j]==2:
        c+=a[i][j];
        #print(i,j);
        findpath(i+1,j,c);
    else:
        c+=a[i][j];
        #print(i,j)
        findpath(i, j+1,c)
        #print(i,j)
        findpath(i+1,j,c)
findpath(0,0,c)
print(a1)
