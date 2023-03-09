numdef=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
s1=input().split()
s2=[]
for x in s1:
    if x.isdigit():
        y=int(x)
        s2.append(numdef[y])
    else:
        s2.append(x)


str1=" ".join(s2)
print(str1)
        
    
