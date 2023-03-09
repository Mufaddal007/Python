a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
#a=[[5,11,30],[5,19,19]]
row=4
col=4
l,r,u,d=0,col-1,0,row-1
i,j=0,0
k=0
direc='r'
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
while k<(row*col):
    
    if direc=='r':
        print(a[i][j], end=" ")
        k+=1
        if j+1>r: direc='d'; i+=1; u+=1; continue;
        j+=1
    elif direc=='d':
        print(a[i][j], end=" ")
        k+=1
        if i+1>d: direc='l'; j-=1; r-=1; continue;
        i+=1
    elif direc=='l':
        print(a[i][j], end=" ")
        k+=1
        if j-1<l: direc='u'; i-=1; d-=1; continue;
        j-=1
    elif direc=='u':
        print(a[i][j], end=" ")
        k+=1
        if i-1<u: direc='r'; j+=1; l+=1; continue;
        i-=1
