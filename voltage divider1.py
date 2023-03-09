def adjvalue(a):
    a=float(str(a)[:str(a).index('.')+3])
    if a<1000:
        return str(a)
    elif a>999:
        return str(a/1000)+'k'
    elif a>999999:
        return str(a/1000000)+'M'
print('''
                V
                |
                |
        _    _  |
        |  r1 | >
      R |     - > <------
        |r2 /r| >       |
        -     - |       |
                |       v
                |       |
                |       |
               0---------
                   --- 
                    -
                    
                    ''')
def potbased() :

    V,v,R,r=input("Enter the values in the following format V v R r: ").split()
    

    if 'k' in r:
        r=float(r[:-1])*1000
    elif 'M' in r:
        r=float(r[:-1])*1000000
    if 'k' in R:
        R=float(R[:-1])*1000
    elif 'M' in R:
        R=float(R[:-1])*1000000
        
    if v=='?':
        V=float(V)
        v=(r*V)/R
        a=v[:v.index('.')+3]
        print("Voltage drop across r: ",a)
    elif R=='?':
        V=float(V); v=float(v)
        R=(r*V)/v
        R=adjvalue(R)
        print("Total value for preset or POT is: ",R)
    elif r=='?':
        V=float(V);  v=float(v)
        r=(R*v)/V
        r=adjvalue(r)
        print("Requred value of resistance for {} volt drop is {} ohm".format(v,r))
    elif V=='?':
        v=float(v)
        V=(v*R)/r
        a=V[:V.index('.')+3]
        print("Potential difference between the two nodes is: {}".format(a))
    print("===================================================================")
        
def fixedvaluebased() :
    V,v,r1,r2=input("Enter the values in the following format V v r1 r2: ").split()
    if 'k' in r1:
        r1=float(r1[:-1])*1000
    elif 'M' in r1:
        r1=float(r1[:-1])*1000000
    if 'k' in r2:
        r2=float(r2[:-1])*1000
    elif 'M' in r2:
        r2=float(r2[:-1])*1000000

    if v=='?':
        V=float(V)
        v=(r2*V)/(r1+r2)
        a=v[:v.index('.')+3]
        print("Voltage drop across r: {}".format(a))
    elif r1=='?':
        V=float(V); v=float(v)
        r1=r2((V/v)-1)
        r1=adjvalue(r1)
        print("Total value for preset or POT is: ",r1)
    elif r2=='?':
        V=float(V); v=float(v)
        r2=(v*r1)/(V-v)
        r2=adjvalue(r2)
        print("Requred value of resistance for {} volt drop is {} ohm".format(v,r2))
    elif V=='?':
        v=float(v)
        V=(v*(r1+r2))/r2
        a=V[:V.index('.')+3]
        print("Potential difference between the two nodes is: {}".format(a))
    print("===================================================================")
        


while(1):
    c=input("What type of voltage divider you want, fixed value based (f) or Pot based (p)?")
    if c.lower()=='f':
        fixedvaluebased()
    elif c.lower()=='p':
        potbased()


    



    
