import math
y=3
pc=0
lc=2
cnt=2
for x in range(1,y):
    pc=int(3*lc)
    lc=int(pc/2)
    cnt+=lc

print(cnt)
