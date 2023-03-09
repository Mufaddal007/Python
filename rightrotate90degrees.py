a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
temp=[]
j=len(a)-1
for x in a:
    print(x)
print("Rotated Anticlockwise: ")
for x in range(len(a)**2):   #rotate anticlockwise
    i=x%len(a)
    temp.append(a[i][j])
    if (x+1)%len(a)==0:
        j-=1
        b.append(temp)
        temp=[]
for x in b:
    print(x)
print()
b=[]
j=0
print("Rotated Clockwise: ")
for x in range(len(a)**2):    #rotate clockwise
    i=len(a)-1-x%len(a)
    temp.append(a[i][j])
    if (x+1)%len(a)==0:
        j+=1
        b.append(temp)
        temp=[]
for x in b:
    print(x)

 

        
        
