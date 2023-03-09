import math
str1=input().split()
i=0
for x in str1:
    z=0
    for y in x:
        if y.isalpha() and y not in ['.','?']:
            z+=1
    i+=z        

i=i/len(str1)
print(math.ceil(i))
    
