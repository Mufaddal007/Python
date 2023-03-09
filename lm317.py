def adjvalue(a):
    if a<1000:
        return a
    elif a>999:
        s=str(a/1000)+'K'
        return s
    elif a>999999:
        s=str(a/1000000)+'M'
        return s
    
print('''pin connection :
                              Vin(L) Adj.(R) Vout(C)
                                __________________
                                |        |       |
                                |        |--R1-- |
                                |    |   |       |
                             0.1uF   R2<-|      1uF
                                |____|___________|
                                      _____
                                       ___
                                        _   ''')                             
while 1 :
    v,r1,r2=input("Enter values in the format Vout R1 R2: ").split()
    print("\n Max. Output voltage = {} \n R1= {} \n R2= {} \n".format(v,r1,r2))
    if 'k' in r1:
        r1=int(r1[:-1])*1000
    elif 'M' in r1:
        r1=float(r1[:-1])*1000000
    if 'k' in r2:
        r2=float(r2[:-1])*1000
    elif 'M' in r2:
        r2=float(r2[:-1])*1000000
    if  v!='?' and r2!='?' and r1!='?':
        v=float(v)
        r1=float(r1)
        r2=float(r2)
        c=1.25*(1+r2/r1)
        if c==v:
            print("Provided values satisfy the equation of LM317, parameters are correct!")
        else : print("Provied values does not satisfy the equation. try again.")
    
    if v=='?':
        r1,r2=int(r1),int(r2)
        v=1.25*(1+r2/r1)
        print("voltage range 1.25V - {} ".format(v))
    elif r2=='?':
        v,r1=int(v),int(r1)
        r2=((v/1.25)-1)*r1
        r2=adjvalue(r2)
        print("Required R2 value is {} ohm ".format(r2))
        
    elif r1=='?':
        v,r2=int(v),int(r2)
        r1=(1.25*r2)/(v-1.25)
        r1=adjvalue(r1)
        print("Required R1 value is {} ohm ".format(r1))

        
    print("=============================================================================================================")



