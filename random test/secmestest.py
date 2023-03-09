aldef=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s1=[]
str1=input().lower()
for x in str1:
    if x.isalpha():
        s1.append(aldef[25-aldef.index(x)])
    elif x.isspace():
        s1.append(x)

print("".join(s1))
