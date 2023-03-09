h=5
m=00
ones=['chk','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
gtens=['chk','eleven','tweleve','thirteen','fourteen','fifteen','sisteen','seventeen','eighteen','nineteen']

s=ones[h]
if m in [15,30,45,00]:
    if m==15:
        s=' quarter past '+s
    elif m==00:
        s=s+" o' clock"

    elif m==30:
        s=' half past '+s

    elif m==45:
        s=' quarter to '+s
elif m<10:
    s=ones[m]+' minutes past '+s
elif 10<m<20:
    s=gtens[m%10]+' minutes past '+s

elif 20<m<30:
    s='twenty'+ones[m%10]+' minutes past '+s
elif 30<m<40:
    s='thirty'+ones[m%10]+' minutes past '+s
elif 40<m<45:
    s='fourty'+ones[m%10]+' minutes past '+s
elif m>45:
    t=60-m
    if t>10:
        t=60-m
        s=gtens[t%10]+' minutes to '+ones[h+1]
    elif t<10:
        s=ones[t]+' minutes to '+ones[h+1]
        
    
print(s) 
    

