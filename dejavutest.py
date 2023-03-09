str1=input()
str2=list(str1)
str2.sort()
rep=False
y=" "
for x in str2:
    if y==x:
        rep=True
        break
    else:
        y=x
         
if rep==True:
    print("Deja Vu")
elif rep==False:
    print("Unique")
    
