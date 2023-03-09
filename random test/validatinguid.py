n=int(input())

s1=[]
for x in range(n):
    s1.append(input())
final=[]

for x in s1:
    check="True"
    repchk=[]
    uc=[]
    di=[]
    if x.isalnum():
        for y in x:
            if not(y in repchk):            
                if y.isalpha():
                    uc.append(y)
                    repchk.append(y)
                elif y.isdigit():
                    di.append(y)
                    repchk.append(y)
                    
                else:
                    check="False"
                    break
            else:
                    check="False"
                    break

    else:
        check="False"
        
    if len(di)>=3 and len(uc)>=2 and len(x)==10 and check=="True":
        final.append("Valid")
    else:
        final.append("Invalid")
        check="True"
    print(repchk)
for x in final:
    print(x)

#test case inputs
#2
#B1CD102354
#B1CDEF2354
