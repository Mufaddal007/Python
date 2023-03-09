num=input()
str1=input()
numarr=str1.split()
numset=set(numarr)
y=0
for x in numset:
    y+=int(x)

out=y/len(numset)
print(out)
