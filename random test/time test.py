y=0
for x in range(25):
    
    if x<12:
        y=str(x)+":30 "+"AM"
    elif x>12:
        y=str(x-12)+":30 "+"PM"
    elif x==12:
        y=str(x)+":30 "+"PM"
    str1=y
    arr=str1.split()
    arr2=arr[0].split(':')
    hc=0
    if len(str(arr2[0]))==1:
        hour='0'+str(arr2[0])
    else:    
        hour=int(arr2[0])
    minutes=arr2[1]

    if arr[1]=="PM" and hour!=12:
        hours=12+int(hour)
    elif hour==12 and arr[1]=="AM":
        hours="00"
    else:
        hours=hour

    str2="{}:{}".format(hours,minutes)
    print(str2)
    
        

