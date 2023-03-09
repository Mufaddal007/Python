str1=input()
digit=[]
spechar=[]

for x in str1:
    if x.isdigit():
        digit.append(x)
    elif x in ['!','@','#','$','%','&','*']:
        spechar.append(x)

if len(digit)>=2 and len(spechar)>=2 and len(str1)>=7:
    print("Strong")
else:
    print("Weak")
                
