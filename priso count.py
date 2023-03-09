n=3
k=7
s=3
pris=0
pri = 0
if k>n:
    pris=k%n
else:
    pris = k
if pris+s-1>n :
    pri = (pris+s-1) - n
elif pris+s-1==n:
    pri=1
else :
    pri = pris+s-1
print(pri)
