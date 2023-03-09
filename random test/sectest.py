str1=input()
check="Quite"
for x in str1:
    if x=='$':
        str2=str1[str1.index(x):]
        for y in str2:
            if y=='t':
                check="Alarm"
                break
            elif y=='g':
                check='Quite'
                break
        break

    elif x=='t':
        str2=str1[str1.index(x):]
        for y in str2:
            if y=='m':
                check="Alarm"
                break
            elif y=='g':
                check='Quite'
                break
        break    

print(check)

    
