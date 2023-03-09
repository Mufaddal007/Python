arr=['abcdde','baccd','eeabg']
c1=0
for x in arr[0]:
    c=0
    for y in arr[1:]:
        if x in y:
            c+=1
           
    if c==len(arr)-1:
        c1+=1

print(c1)
