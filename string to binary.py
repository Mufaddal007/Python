while 1:
    print("What do you want to perform?")
    c=input("press 'b' to get to binary code \n press 's' to get original string ")
    if c=='b':
        s=input("String :")                        #E 
        s1=''                                      #N
        for x in s:                                #C   
            s2=str(bin(ord(x)))                    #O  
                                                   #D
            s1+=s2[s2.index('b')+1:].rjust(7,'0')  #E
        print("Binary code")                       #R  
        print(s1)
    
    elif c=='s':                                   #D
        s4=input("Binary code:")                   #E
        s3=''                                      #C
        for x in range(0,len(s4), 7):              #O
            s5=s4[x:x+7]                           #D
            s3+=chr(int(s5, 2))                    #E  
        print("Original string:")                  #R 
        print(s3)                            
    else:
        print("Invalid input, try again.")
            

