for x in range(24):
    if x<=12:
        str1="{}:05:45AM".format(x)
        arr2=str1.split(':')
    elif x>12 and x<=24:
        p=x-12
        str1="{}:05:45PM".format(p)
    if len(str(arr2[0]))==1:
        hour='0'+arr2[0]
    else:
        hour=int(arr2[0])
    minutes=arr2[1]
    seconds=arr2[2][:2]
    nchk=arr2[2:]
        
    if nchk=="PM" and hour!=12 :    
        time=12+int(hour)
    elif hour==12 and nchk=="AM" :
        time="00"
    else:    
        time=hour
    str2="{}:{}:{}".format(time,minutes,seconds)
    print(str2)
