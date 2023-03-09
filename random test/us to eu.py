mondef=['check','January','February','March','April','May','June','July','August','September','October','November','December']
str1=input()
if '/' in str1:
    dd=str1[:str1.index('/')]
    str2=str1[str1.index('/')+1:]
    mm=str2[:str2.index('/')]
    year=str2[str2.index('/')+1:]
    print(mm+'/'+dd+'/'+year)

else:
    s1=str1.split()
    s2='/'.join(s1)
    s3=s1[1]+"/"+str(mondef.index(s1[0]))+"/"+s1[2]
    s4=s3.replace(",","")
    print(s4)
