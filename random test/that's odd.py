n=int(input())
arr1=[]
for x in range(n):
    arr1.append(int(input()))
z=0    
for x in arr1:
    if x%2==0:
       z+=x

print(z)       
