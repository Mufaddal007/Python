def lessthanone(a):
    b=a
    i=0
    if b<1:
        while(1):
            b*=10
            i+=1
            if b>=1 and i%3==0:
                b=str(b)
                if i//3==1: b=b[:b.index('.')+3]+'m'
                elif i//3==2: b=b[:b.index('.')+3]+'u'
                elif i//3==3: b=b[:b.index('.')+3]+'n'
                break
    return b
    
def adjvalue(a):
    a=str(a)
    a=a[:a.index('.')+3]
    a=float(a)
    if a<1000: return str(a)
    elif a>999: return str(a/1000)+'k'
    elif a>999999: return str(a/1000000)+'M'
    
print('''

    Vcc= 5V - 15V ___________________
                  |       |         |
               ___|_______|____     >   R1
              |   4       8    |    >
              |              7 |----|    
   OUTPUT  ---| 3              |    |
              |     NE555      |    >
          |---| 5              |    >   R2
  0.01uF  =   |              6 |----|
          |   |__1_________2___| |   |
        ------   |         |     |   = C1
         ---   -----       |-----|   |
          -     ---                -----
                 -                  ---
                                     -
''')

while(1):
    T,R1,R2,C1=input("Enter the values in the format T R1 R2 C1 (enter question mark (?) for unknown value): ").split()
    if 'k' in R1: R1=str(float(R1[:-1])*1000)
    elif 'M' in R1: R1=str(float(R1[:-1])*1000000)
    if 'k' in R2: R2=str(float(R2[:-1])*1000)
    elif 'M' in R2: R2=str(float(R2[:-1])*1000000)
    if 'uF' in C1: C1=str(float(C1[:-2])*(10**(-6)))

    if T=='?':
        R1=float(R1)
        R2=float(R2)
        C1=float(C1)
        T=0.693*(R1+2*R2)*C1    
    elif R1=='?':
        T=float(T)
        R2=float(R2)
        C1=float(C1)
        R1=(T/(0.693*C1))-2*R2
    elif R2=='?':
        T=float(T)
        R1=float(R1)
        C1=float(C1)
        R2=((T/(0.693*C1))-R1)/2
    elif C1=='?':
        T=float(T)
        R1=float(R1)
        R2=float(R2)
        C1=(T/(0.693*(R1+2*R2)))

    Th=0.693*(R1+R2)*C1
    Tl=T-Th
    C1=lessthanone(C1)
    F=str(1/T)
    F=F[:F.index('.')+3]
    DutyCycle=str(Th/T*100)
    DutyCycle=DutyCycle[:DutyCycle.index('.')+3]
    Th=lessthanone(Th)
    Tl=lessthanone(Tl)
    #DutyCycle=1-(R2/(R1+R2))
    T=lessthanone(T)
    R1=adjvalue(R1)
    R2=adjvalue(R2)

    print("\033[1m 1)Value of R1 is: {}ohm \n2)Value of R2 is: {}ohm\n3)Value of C1 is: {}F \n4)Output High time: {} and Output Low time: {} \n5)Duty Cycle of waveform: {} \
          \n6)Time period of the waveform is: {}s \n7)Frequency of oscillation is: {}Hz \033[0m".format(R1,R2,C1,Th,Tl,DutyCycle,T,F))
    print("=================================================================================================================================")
    c=input("Do you want to run this program again? press any key  to continue or  q to quit").lower()
    if c=='q': break
    else : continue
    






    
    


    
