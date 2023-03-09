chars=['A','B','C', 'D', 'E', 'F']
def find_char(num):
    if num<10:
        return str(int(num))
    return chars[int(num%10)]
def find_string(n1,n2,k,negative_flag=0, after_decimal_flag=0):
    bd=[]
    ad=[]
    while n1>=k:
            r=n1%k
            n1=int((n1-r)/k)
            bd.append(find_char(r))
    bd.append(find_char(n1))
    bd.reverse()
    if negative_flag:
        for x in range(len(bd)):
            if not bd[x].isdigit(): a=15-(10+chars.index(bd[x]))
            else: a=15-int(bd[x])
            bd[x]=find_char(a)
    if not after_decimal_flag: return ("".join(bd))
    i=0
    while n2!=1 and i<4:
        n2=n2*k
        ad.append(find_char(n2))
        n3='0.'+str(n2)[str(n2).index('.')+1:]
        n2=float(n3)
        i+=1
    return ("".join(bd))+'.'+("".join(ad))
    

while 1:
    n=float(input("Enter figure in decimal to be converted into another base system:"))
    k=int(input("Enter the base in which you want your output:"))
    if not (2<=k<=16):
        print("Invalid base value")
        continue
    f1=0
    f2=0
    n1=int(str(n)[:str(n).index(".")])
    n2=n-int(n)
    n3=str(n)[str(n).index(".")+1:]
    if n1<0:
        n1=(-1)*n1
        f1=1
    if int(n3)>0: f2=1
    
    s=find_string(n1,n2,k,f1,f2)
        
    print("Your answer is : {}".format(s))
    print('\n')
        
            


