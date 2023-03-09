a=[-5, 4, 6, -3, 4 , -1]
n=6
maxsum=0
c=0
for x in range(n):
    if c+a[x]>0:
        c+=a[x]
        maxsum=max(c, maxsum)
    else:
        c=0
print(maxsum)
