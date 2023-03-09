n=int(input("enter num of inputs---->"))
str1=[]
str2=[]
for x in range(0,n):
    command=input()
    str1.append(command)

for x in str1:
    if "insert" in x:
        str3=str(x)
        str4=str3.split()
        i=int(str4[1])
        v=int(str4[2])
        str2.insert(i,v)
    elif "append" in x:
        str5=str(x)
        str6=str5.split()
        v=int(str6[1])
        str2.append(v)
    elif "print" in x:
        print(str2)
    elif "remove" in x:
        str2.remove(str2[0])
    elif "pop" in x:
        str2.pop()
    elif "reverse" in x:
        str2.reverse()
    elif "sort" in x:
        str2.sort()
    
