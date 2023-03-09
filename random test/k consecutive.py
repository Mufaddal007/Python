i=int(input())
fin=[]
for x in range(i):
    s=input().split()
    k=int(s[1])
    n=str(input())
    nums=[]
    x=0
    while x<len(n)-k:
           nums.append(n[x:x+k])
           x+=1
    check=0
    for x in nums:
        w=list(x)
        m=1
        for x in w:
            m*=int(x)
        if m>check:
            check=m
    #print(nums)
    fin.append(check)
for x in fin:
    print(x)


