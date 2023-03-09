str1=input()
s2=[]
for x in range(len(str1)):
    if  not(str1[len(str1)-x-1] in ['=','/']):
        s2.append(str1[len(str1)-x-1])

    elif str1[len(str1)-x-1] in ['=','/']:
        break

s2.reverse()
print("".join(s2))
              
