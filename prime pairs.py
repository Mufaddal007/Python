n=5
b=[]
def isprime(a):
    for x in range(2,int(a**0.5)+1):
        if a%x==0: return 0
    return 1
for x in range(2,n//2+1):
    if isprime(x) and isprime(n-x):
        b.append([x,n-x])
print(b)
