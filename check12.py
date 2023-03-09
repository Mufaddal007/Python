while 1:
    arr=input().split()
    s1='{'
    for x in arr:
        s='0b'
        for y in x:
            if y!=',' and y!='{':
                s+=str(y)
        s1+=' '+s+','
    s2=s1[:-1]
    print(s2)

