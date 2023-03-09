circuit='([1,2,5],[3,6],2)'
value=0
opening=[]
closing=[]

def find_val(a,b,flag=0):
    if flag: temp= opening[0]
    else: temp=closing[a-1]
    if circuit[closing[a]]==']': 
        if not flag : b=pow(b,-1)
        for x in circuit[temp+1: closing[a]]:
            if x.isdigit(): b+=pow(int(x),-1) 
        b=pow(b,-1)
    elif circuit[closing[a]]==')':
        for x in circuit[temp+1: closing[a]]:
            if x.isdigit(): b+= int(x)
    return b
for x in range(len(circuit)):
    if circuit[x] in ('[','('): opening.append(x)
    elif circuit[x] in (']',')'): closing .append(x)
opening.reverse()
value=find_val(0,value,flag=1)
for x in range(1,len(opening)): 
    value=find_val(x,value,flag=0)
    
print(value)

    