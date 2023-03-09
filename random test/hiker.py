s='UDDDUDUU'
dc=0
uc=0
vcnt=0
for x in s:
    if x=='D':
        dc+=1
    if x=='U':
        uc+=1
        if uc==dc:
            vcnt+=1
            dc=0
            uc=0
print(vcnt)
