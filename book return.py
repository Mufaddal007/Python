n=input().split()
n1=input().split()
fine=1
if int(n[2])!=int(n1[2]):
    fine=10000
elif int(n[2])==int(n1[2]) and int(n[1])!=int(n[1]):
    fine=500*(int(n[1])-int(n1[1]))
elif int(n[0])!=int(n1[0]) and int(n[1])==int(n1[1]) and int(n[2])==int(n1[2]):
    fine=abs(15*(int(n[0])-int(n1[0])))
elif n1==n:
    fine=0
print(fine)
