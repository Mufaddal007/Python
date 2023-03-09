n=int(input())
dict1={}
for x in range(n):
    s=input().split()
    dict1[s[0]]+=int(s[1])

print(dict1)
