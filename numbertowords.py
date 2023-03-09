undertwenty=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
weight=['', 'Thousand', 'Million', 'Billion','Trillion','Quadrillion', 'Quintillion','Sextillion', 'Septillion', 'Octillion', 'Nonillion','Decillion','Unidecillion','Duodecillion','Tredecillion','Quatttuor-decillion','Quindecillion','Sexdecillion','Septendecillion','Octodecillion','Novemdecillion','Vigintillion']

def twentymark(x,b, flag=0,zeroflag=0):
    s=[]
    if flag:
        if b>19: s+=[tens[threes[0]],undertwenty[threes[1]]]
        elif b<20: s.append(undertwenty[b])
        return s    
    if not zeroflag:s+=[undertwenty[groups[x][0]],'hundred']
    elif zeroflag: s+=''
    if b>19: s+=[tens[groups[x][1]],undertwenty[groups[x][2]]]
    elif b<20: s.append(undertwenty[b])
    return s

while  1:
    threes=[]
    groups=[] 
    n=int(input("Enter the number to get in words: "))
    i=0
    while n:
        i+=1
        if i%3==0:
            threes.append(n%10)
            threes[:]=threes[::-1]
            groups.append(threes) 
            threes=[]
        elif i%3==1 or i%3==2:
            threes.append(n%10)
        n=n//10
    threes[:]=threes[::-1]
    s=[]
    if threes:
        if len(threes)==1: s+=[undertwenty[threes[0]]]
        elif len(threes)==2:
            b=threes[0]*10+ threes[1]
            s+=twentymark(1,b,flag=1) 
        elif len(threes)==3:
            b=threes[1]*10+threes[2] 
            s+=twentymark(-1,b,flag=0,zeroflag=0)
        s.append(weight[len(groups)])
    groups.reverse()
    #print(threes, groups)
    for x in range(len(groups)):
        b=groups[x][1]*10+ groups[x][2] 
        if groups[x][0]==groups[x][1]==groups[x][2]==0: continue
        if groups[x][0]==0: s+=twentymark(x,b,zeroflag=1)
        else: s+=twentymark(x,b)
        s.append(weight[len(groups)-x-1])
    s1=' '.join(s)
    print(s1)
    


