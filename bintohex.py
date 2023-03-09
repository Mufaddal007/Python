while(1):
    s=input()
    if s=='stop':
        break
    else:
        
        arr=s.split()
        
        s1=''
        s4=''
        for x in arr:
            z=list(x)
            z.reverse()
            for y in x:
                if y not in ('{','}',',',';'):
                    s1+=y
            for y in z:
                if y not in  ('{','}',',',';'):
                    s4+=y
            s1+=' '
            s4+=' '
        #print('oribin', s1)
        #print('revbin', s4)
        
        arr2=s1.split()
        arr3=s4.split()
        s3='{'
        i=0
        for x in arr2:
            s2=hex(int(x,2)).ljust(5,' ')
            if i<4:
                s3+=s2+','
                i+=1
            else:
                s3+=s2
        s3+='};'
        s5='{'
        for x in arr3:
            s2=hex(int(x,2)).ljust(5,' ')
            if i<4:
                s5+=s2+','
                i+=1
            else:
                s5+=s2
        s5+='};'

        #print('orihex', s3)
        #print('revhex', s5)
        print(s5)

        #print(' ')
