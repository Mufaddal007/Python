chars=['A','B','C', 'D', 'E', 'F']
def find_char(num):
    if num<10:
        return str(int(num))
    elif num>=10:
        return chars[int(num%10)]
while 1:
    ad=[]
    bd=[]
    post_decimal=True
    n=float(input("Enter figure in decimal to be converted into another base system:"))
    k=int(input("Enter the base in which you want your output:"))
    if not (2<=k<=16):
        print("Invalid base value")
        
    else :
        n1=int(str(n)[:str(n).index(".")])
        n2=n-int(n)
        n4=str(n)[str(n).index(".")+1:]
        if int(n4)==0:
            post_decimal=False
        r=n
        i=0
        while n2!=1 and i<4:
            n2=n2*k
            ad.append(find_char(n2))
            n3='0.'+str(n2)[str(n2).index('.')+1:]
            n2=float(n3)
            i+=1
        while n1>=k:
            r=n1%k
            n1=int((n1-r)/k)
            bd.append(find_char(r))
        bd.append(find_char(n1))
        bd.reverse()
        if post_decimal:
            s=("".join(bd))+'.'+("".join(ad))
        else:
            s=("".join(bd))
        print("Your answer is : {}".format(s))
        print('\n')
        
            


