a=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
tens1=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
tens2=['once','ten','hundred','thousand','ten thousand','Lac','ten lac','Crore', 'Ten crore']

while(1):
    b=int(input())    
    s=''
    i=1
    while i<len(str(b))-1:
        check=True
        
        c=int(b/(10**(len(str(b))-i)))%10
        d=(len(str(b))-i)
        #print(a[c],d)
        if c==0 :
            i+=1
            continue
            
        if d in (4,6,8):
            f=int(b/(10**(d-1)))%100
            if f<20:
                s+=a[f]+' '+tens2[d-1]+' '
                check=False
            else:
                f1=int(f/10)
                f2=f%10
                #print(f,f1,f2)
                s+=tens1[f1]+' '
                
                s+=a[f2]+' '+tens2[d-1]+' '
                check=False
                
        else:
            s+=a[c]+' '+tens2[d]+' '
        if check:
            i+=1
        else :
            i+=2
                
    e=b%100
    if b<20:
        #print(a[b])
        s+=a[b]+' '
    elif b>20:
        #print(tens1[int(e/10)])
        #print(a[e%10])
        s+=tens1[int(e/10)]+' '+a[e%10]

    print(s.title())
    

        
        


