morse_alpha={'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111', \
             'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1', \
             'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100'}
alpha_keys=list(morse_alpha.keys())
alpha_values=list(morse_alpha.values())
morse_nums={'0': '01111', '1': '00111', '2': '00011', '3': '00001', '4': '00000', '5': '10000', '6': '11000', '7': '11100', '8': '11110', \
            '9': '11111'}
num_keys=list(morse_nums.keys())
num_values=list(morse_nums.values())
while 1:
    c=input("What do you wnat to perform ?\nPress M to get morse code , press S to get original string: \n").upper()
    if c=='M':
        s=input("Enter String to get morse code: ").strip().upper()                        #E
        s1=''                                                                              #N
        for x in s:                                                                        #C
            if x.isalpha():                                                                #O
                s1+=morse_alpha[x]+' '                                                     #D 
            elif x.isdigit():                                                              #E 
                s1+=morse_nums[x]                                                          #R  
        print("Morse code equivalent: \n======>{}".format(s1))

    elif c=='S':                                                         
        m=input("Enter morse code: ").split()             
        s3=''                                                      #DE
        for x in m:                                                #CO
            s3+=alpha_keys[alpha_values.index(x)]                  #DE 
        print("original string: \n======>{}  ".format(s3))         #R 
    elif c=='Q':
        break
    else :
        print("Invalid input ")
    print("\n \n")
    
