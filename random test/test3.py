str1="geluhelugeluheluram"
str2="gelu"
j=0
while True:
    if (str1.find(str2)!=(-1)):
        j+=1
        str1=str1[str1.index(str2)+1:]
    else:
         break


print(j)        
 
        
    
    
