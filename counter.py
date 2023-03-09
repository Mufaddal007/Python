s='aaabbbccddd'
s2=''
for x in s:
    if s.count(x)%2!=0:
        s2+=x*(s.count(x)%2)


print(s2)
        
     
            
