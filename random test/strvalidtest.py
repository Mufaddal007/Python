#taking input and declaring arrays
n=int(input())
octarr=[]
hexarr=[]
binarr=[]
narr=[]
finalarr=[]
a=bin(n)-
lenarr=[]
for x in a:
    lenarr.append(x)
b=len(lenarr)
octarr1=[]
hexarr1=[]
binarr1=[]
narr1=[]

#finding hex oct and bin codes and storing them in their respective arrays
#with rjust method of declared width
for x in range(1,n+1):

    narr.append(str(x))
    hexarr.append(str(hex(x)[hex(x).index("x")+1:]).capitalize())
    octarr.append(str(oct(x)[oct(x).index("o")+1:]))
    binarr.append(str(bin(x)[bin(x).index("b")+1:]))


for x in range(1,n+1):
    narr1.append(narr[x-1].rjust(b," "))
    hexarr1.append(hexarr[x-1].rjust(b," "))
    octarr1.append(octarr[x-1].rjust(b," "))
    binarr1.append(binarr[x-1].rjust(b," "))

#creating string for each line and finalizing output
for x in range(len(narr1)):
    finalstr="{} {} {} {}".format(narr1[x],octarr1[x],hexarr1[x],binarr1[x]).rstrip()
    finalarr.append(finalstr)

#priting final array

for x in finalarr:
    print(x)


