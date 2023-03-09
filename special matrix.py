n=2;
m=1;
c=0
class solution:
    c=0
    blocked_cells=[1,1]
    def findpath(self,i,j):
        #print(i,j)
        if i==n-1 and j==m-1:
            #print('Path found');
            self.c+=1; return 1;
        if i==n or j==m: return 0
        #if i+1<n:
        if ([i+1,j] not in self.blocked_cells): self.findpath(i+1,j)
        #if j+1<m:
        if ([i,j+1] not in self.blocked_cells): self.findpath(i,j+1)

obj=solution()        
obj.findpath(0,0);
print(obj.c)
