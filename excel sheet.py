chars=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a=int(input())
s=''
while(a>26):
    s+=chars[a%26]
    a=a//26
s+=chars[a]
s=s[::-1]
print(s)
