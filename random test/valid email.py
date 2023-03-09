n=int(input())
a=[]
for x in range(n):
    s=input()
    name=s[:s.index('@')]
    websitename=s[s.index('@')+1:s.index('.')]
    extension=s[s.index('.')+1:]
    namebool=True
    webnamebool=True
    extensionbool=True
    for x in name:
        if (not x.isalpha()) and  (not x.isdigit()) and (x not in ['-', '_']):
            namebool=False
            print(x)
            break
    for x in websitename:
        if (not x.isalpha()) and  (not x.isdigit()):
            print(x)
            webnamebool=False
            break

    if len(extension)>3:
        extensionbool=False

     
    print(namebool, webnamebool, extensionbool)
    if namebool and webnamebool and extensionbool:
        a.append(s)

print(a)
