n,temp,separated=int(input()),'',''
while n:
    if len(temp)==2:
        temp+=str(n%10)
        separated,temp,n=separated+temp+',','',n//10
        continue
    temp,n=temp+str(n%10),n//10
separated+=(temp)
separated=separated[::-1]
if separated[0]==',': separated=separated[1:]
print(separated)
