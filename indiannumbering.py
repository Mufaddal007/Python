undertwenty=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
weight=['thousand','lac','crore','Hundred']
def twentymark(x,y,b,flag=0):
    s=[]
    if flag:
        if b>19: s+=[tens[firstthree[1]], undertwenty[firstthree[2]]]
        elif b<20: s.append(undertwenty[b])
    else:
        if b>19: s+=[tens[groups[x][y]],undertwenty[groups[x][y+1]]]
        if b<20: s.append(undertwenty[b])
    return s
while 1:
    n=int(input())
    firstthree=[]
    twos=[]
    groups=[]
    i=0

    while n:

        if i>2:
            if i%2==1: twos.append(n%10)
            else: 
                twos.append(n%10)
                twos.reverse()
                groups.append(twos)
                twos=[]
        else:
            firstthree.append(n%10)
        
        n,i=n//10,i+1
    s=[]
    
    if twos: groups.append(twos)
    firstthree.reverse()
    if len(groups[-1])==1: 
        s.append(undertwenty[groups[-1][0]])
    else:
        b=groups[-1][0]*10+groups[-1][1]
        s+=twentymark(-1,0,b)
    s.append(weight[len(groups)-1])
    groups.pop()
    groups.reverse()
    for x in range(len(groups)):
        if groups[x][0]==groups[x][1]==0: continue
        b=groups[x][0]*10+groups[x][1]
        s+=twentymark(x,0,b)
        s.append(weight[len(groups)-x-1])
        
    if not firstthree[0]==0: 
        s+=[undertwenty[firstthree[0]],'Hundred']
        b=firstthree[1]*10+firstthree[2]
        s+=twentymark(1,2,b,flag=1)
    else: 
        b=firstthree[1]*10+firstthree[2]
        s+=twentymark(1,2,b,flag=1)
        
    print(' '.join(s))


        
