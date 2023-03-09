chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s='We promptly judged antique ivory buckles for the next prize'.lower()
chk=True
for x in chars:
    
    if x not in s:
        chk=False
        break

if chk:
    print('pangram')
else:
    print('not pangram')
