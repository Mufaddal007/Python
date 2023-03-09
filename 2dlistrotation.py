nums=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n=4
i=0
j=0
#a=0
#b=0
a1=[[0 for x in range(n)] for x in range(n)]
for x in range(n):
    i=-x
    j=(n-1)-x
    for y in range(n):
        #a=x+i
        #b=y+j
        a1[x+i][y+j]=nums[x][y]
        #print(a,b, nums[x][y])
        i+=1
        j-=1
    #print()
[print('{}          {}'.format(nums[x],a1[x])) for x in range(n)]

