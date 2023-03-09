def bubblesort1(a):
    for x in range(len(a)):
        for y in range(len(a)-1):
            if a[y]>a[y+1]:
                temp=a[y]
                a[y]=a[y+1]
                a[y+1]=temp

def bubblesort2(a):
    for x in range(len(a)):
        for y in range(len(a)-x-1):
            if a[y]>a[y+1]:
                temp=a[y]
                a[y]=a[y+1]
                a[y+1]=temp
    
def bubblesort3(a):
    for x in range(len(a)):
        for y in range(x+1,len(a)):
            if a[x]>a[y]:
                temp=a[x]
                a[x]=a[y]
                a[y]=temp
a=[5,4,3,2,1]
bubblesort1(a)
print(a)
a=[10,9,8,7,6]
bubblesort2(a)
print(a)
a=[15,14,13,12,11]
bubblesort3(a)
print(a)


