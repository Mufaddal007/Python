arr=[]
while(1):
    s=input()
    if s=='s':
        break
    else:
        arr1=s.split()
        arr1.reverse()
        s2='{'
        i=0
        for y in arr1:
            s1='0b'
            
            for z in y:
                if not  z in ("'",',','{','}',';'):
                    s1+=z
            i+=1
            if i!=5:
                s1+=', '
            s2+=s1
        s2+='}'
        print(s2)


        

