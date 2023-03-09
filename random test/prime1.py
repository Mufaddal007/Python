prime=[2,3,5]
n=int(input())
fin=[]
for x in range(n):
    test=int(input())
    c=0
    x=4
    while c!=(test-3):
        x+=1
        if x%2!=0 and  x%3!=0 and  x%5!=0 :
            prime.append(x)
            c+=1

        
    fin.append(prime[len(prime)-1])
for x in fin:
    print(x)
print(prime)

